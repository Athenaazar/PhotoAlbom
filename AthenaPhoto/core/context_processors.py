def user_is_authenticated(request):
    if request.user.is_authenticated:
        return {"user_is_authenticated": True}
    return {"user_is_authenticated": False}
