def check_admin(user):
    if user.get("role") != "admin":
        raise PermissionError("Unauthorized")