from django.http import request, Http404
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from dms_site.servises import user_adventure_count


class Mixin:

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        adventure_count = user_adventure_count(request)
        context["adventure_count"] = adventure_count
        return self.render_to_response(context)
