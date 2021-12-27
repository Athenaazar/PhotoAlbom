from django.urls import path
from core.views import CreateCategory, Login, CategoryManagement, DeleteCategory, AddNewPicture, \
    CategoryAllPictures, PictureDetails, Home, Logout

app_name = 'core'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', Home.as_view(), name='home'),
    path('category-management/', CategoryManagement.as_view(), name='category_management'),
    path('create-category/', CreateCategory.as_view(), name='create_category'),
    path('delete-category/', DeleteCategory.as_view(), name='delete_category'),
    path('add-new-picture/', AddNewPicture.as_view(), name='add_new_picture'),
    path('category/pictures/<str:category_uuid>/', CategoryAllPictures.as_view(),
         name='category_all_pictures'),

    path('picture/picture-details/', PictureDetails.as_view(), name='picture_details'),

]
