from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from core.models import Category, Picture
from core.tools import generate_category_code


class Login(View):
    TEMPLATE_NAME = 'login.html'

    def get(self, request):
        return render(request, self.TEMPLATE_NAME, {})

    def post(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            context = {
                "err_message": "some error occurred, please try again."
            }
            return render(request, self.TEMPLATE_NAME, context)
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                context = {
                    "err_message": "username or password is wrong, please try again."
                }
                return render(request, self.TEMPLATE_NAME, context)
            else:
                login(request, user)
                return redirect("core:home")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("core:home")


class Home(View):
    TEMPLATE_NAME = "home.html"

    def get(self, request):
        all_categories = Category.objects.all()
        context = {"all_categories": all_categories}
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request):
        try:
            category_uuid = request.POST['category']
        except:
            messages.error(request, "some error occurred!")
            return redirect("core:home")
        else:
            return redirect("core:category_all_pictures", category_uuid=category_uuid)


class CreateCategory(LoginRequiredMixin, View):
    TEMPLATE_NAME = 'create_category.html'

    def get(self, request):
        context = {}
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request):
        try:
            category_title = request.POST["category_title"]
        except:
            messages.error(request, "you didn't enter any title!")
            return redirect("core:create_category")
        else:
            if len(category_title) > 100:
                messages.error(request, "maximum length of title is 100 letters. ")
            elif len(category_title) == 0:
                messages.error(request, "you didn't enter any title! ")
            else:
                already_category = Category.objects.filter(name=category_title)
                if already_category.exists():
                    messages.error(request, "you already added this category! ")
                else:
                    category = Category.objects.create(
                        code=generate_category_code(),
                        name=category_title
                    )
                    messages.success(request, "new category added successfully.")
            return redirect("core:create_category")


class CategoryManagement(LoginRequiredMixin, View):
    TEMPLATE_NAME = 'category_management.html'

    def get(self, request):
        all_categories = Category.objects.all()
        context = {
            "categories": all_categories
        }
        return render(request, self.TEMPLATE_NAME, context)


class DeleteCategory(LoginRequiredMixin, View):
    def post(self, request):
        try:
            category_uuid = request.POST["category_uuid"]
            category = Category.objects.get(uuid=category_uuid)
        except:
            return JsonResponse({"status": "error", "message_text": "some error occurred!"})
        else:
            category_pictures = category.pictures.all()
            for picture in category_pictures:
                picture.image.delete()
            category.delete()
            messages.success(request, "category successfully removed.")
            return JsonResponse(
                {"status": "ok", "url": "/category-management/"})


class AddNewPicture(LoginRequiredMixin, View):
    TEMPLATE_NAME = "add_new_picture.html"

    def get(self, request):
        all_categories = Category.objects.all()
        context = {"all_categories": all_categories}
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request):
        try:
            category_uuid = request.POST['category']
            category = Category.objects.get(uuid=category_uuid)

            picture_title = request.POST['picture_title']

            loc_latitude = request.POST['latitude']
            loc_longitude = request.POST['longitude']

            selected_picture = request.FILES['picture']

        except:
            messages.error(request, "some error occurred!")
            all_categories = Category.objects.all()
            context = {"all_categories": all_categories}
            return render(request, self.TEMPLATE_NAME, context)
        else:
            all_categories = Category.objects.all()
            context = {"all_categories": all_categories}

            if selected_picture.size > (1024 * 1024 * 10):
                messages.error(request, "picture max size is 10 mb.")
                return render(request, self.TEMPLATE_NAME, context)

            picture = Picture.objects.create(
                category=category,
                title=picture_title,
                image=selected_picture,
                latitude=loc_latitude,
                longitude=loc_longitude,
                size=selected_picture.size
            )
            messages.success(request, "picture successfully added.")
            return render(request, self.TEMPLATE_NAME, context)



class CategoryAllPictures(View):
    TEMPLATE_NAME = "category_all_pictures.html"

    def get(self, request, category_uuid):
        try:
            category = Category.objects.get(uuid=category_uuid)
        except:
            messages.error(request, "some error occurred!")
            return redirect("core:home")
        else:
            all_pictures = category.pictures.all()
            all_categories = Category.objects.all()

            context = {
                "all_pictures": all_pictures,
                "selected_category": category,
                "all_categories": all_categories,
            }
            return render(request, self.TEMPLATE_NAME, context)

    def post(self, request, category_uuid):
        if request.user.is_authenticated:
            try:
                deleting_picture_uuid = request.POST['picture_uuid']
                picture = Picture.objects.get(uuid=deleting_picture_uuid)
            except:
                messages.error(request, "some error occurred!")
                return redirect("core:category_all_pictures", category_uuid=category_uuid)
            else:
                picture.image.delete()
                picture.delete()
                messages.success(request, "picture successfully deleted.")
                return redirect("core:category_all_pictures", category_uuid=category_uuid)
        else:
            messages.error(request, "some error occurred!")
            return redirect("core:category_all_pictures", category_uuid=category_uuid)


class PictureDetails(View):
    TEMPLATE_NAME = "category_all_pictures.html"

    def post(self, request):
        try:
            picture_uuid = request.POST['picture_uuid']
            picture = Picture.objects.get(uuid=picture_uuid)
        except:
            pass
        else:
            context = {
                "current_picture": picture
            }
            return render(request, self.TEMPLATE_NAME, context)
