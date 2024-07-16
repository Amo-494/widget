from django.urls import path
from .views import (
    WaitlistCreateView, WidgetListView, WidgetDetailView,
    NotificationListView, BlogPostListView, ContentEditView,
    EmailTemplateListView, EmailTemplateEditView, UserWidgetsView,
    UserDataExportView, SettingsView
)

urlpatterns = [
    path('waitlist/', WaitlistCreateView.as_view(), name='waitlist-create'),
    path('widgets/', WidgetListView.as_view(), name='widget-list'),
    path('widgets/<int:pk>/', WidgetDetailView.as_view(), name='widget-detail'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('blog/', BlogPostListView.as_view(), name='blog-list'),
    path('content/<int:pk>/', ContentEditView.as_view(), name='content-edit'),
    path('email-templates/', EmailTemplateListView.as_view(), name='email-template-list'),
    path('email-templates/<int:pk>/', EmailTemplateEditView.as_view(), name='email-template-edit'),
    path('users/<int:user_id>/widgets/', UserWidgetsView.as_view(), name='user-widgets'),
    path('users/<int:user_id>/export/', UserDataExportView.as_view(), name='user-data-export'),
    path('settings/<int:user_id>/', SettingsView.as_view(), name='settings'),
]
