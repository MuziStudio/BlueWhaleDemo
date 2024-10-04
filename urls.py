# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib import admin

import moments.views as moments_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", moments_view.home),
    path("user/", moments_view.show_user),
    path("status/", moments_view.show_status),
    path("post/", moments_view.submit_post),
    path("set-su/", moments_view.set_super_user)
]
