from django.urls import path

from . import views

urlpatterns = [
    path("", views.PatientListCreateView.as_view(), name="list_patients"),
    path(
        "<int:pk>/",
        views.PatientRetrieveUpdateDeleteView.as_view(),
        name="patient_detail",
    ),
    path(
        "<int:pk>/labresult/",
        views.LabResultCreate.as_view(),
        name="patient_Create_labresult",
    ),
    path(
        "<int:pk>/listlabresult/",
        views.LabResultList.as_view(),
        name="patient_List_labresult",
    ),
    path(
        "<int:patient_id>/appointements/",
        views.AppointmentListView.as_view(),
        name="patient_ListCreate_appointments",
    ),
     path(
        "<int:patient_id>/appointements/<int:pk>",
        views.AppointmentDetailView.as_view(),
        name="patient_updateRetriveDelete_appointments",
    ),

    # path("current_user/", views.get_posts_for_current_user, name="current_user"),
    # path(
    #     "posts_for/",
    #     views.ListPostsForAuthor.as_view(),
    #     name="posts_for_current_user",
    # ),
]

