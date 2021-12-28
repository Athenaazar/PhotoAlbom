import os
import random
import string


def generate_category_code():
    from core.models import Category

    last_category = Category.objects.last()
    if last_category:
        return last_category.code + 1
    return 1


def generate_hash(hash_length):
    password = string.ascii_letters + string.digits
    password_list = []
    for passChar in range(hash_length):
        pass_random = random.choice(password)
        password_list.append(pass_random)
    final_password = "".join(password_list)
    return final_password


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"pictures/{generate_hash(10)}{ext}"
