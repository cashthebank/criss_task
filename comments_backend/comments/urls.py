from django.urls import path
import comments.views as views

app_name = "comments"

urlpatterns = [
    path("", views.home, name="home"),
    path("about_me", views.about_me, name="about-me"),
    path("contact_me", views.contact_me, name="contact-me"),
    path("comments", views.comments_page, name="comments"),
]
