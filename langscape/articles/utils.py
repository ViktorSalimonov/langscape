# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied


def check_member_rights(request):
    if request.user.member.is_gold:
        request.is_gold = True
        return request

    raise PermissionDenied
