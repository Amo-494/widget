from rest_framework import generics
from .models import User, Waitlist, Widget, Notification, BlogPost, Content, EmailTemplate, Settings
from .serializers import (
    UserSerializer, WaitlistSerializer, WidgetSerializer, NotificationSerializer,
    BlogPostSerializer, ContentSerializer, EmailTemplateSerializer, SettingsSerializer
)

class WaitlistCreateView(generics.CreateAPIView):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer

class WidgetListView(generics.ListAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

class WidgetDetailView(generics.RetrieveAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContentEditView(generics.RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class EmailTemplateListView(generics.ListAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer

class EmailTemplateEditView(generics.RetrieveUpdateAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer

class UserWidgetsView(generics.ListAPIView):
    serializer_class = WidgetSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Widget.objects.filter(userwidget__user_id=user_id)

class UserDataExportView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SettingsView(generics.RetrieveUpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        return Settings.objects.get(user_id=user_id)

