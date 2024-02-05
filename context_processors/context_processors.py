from Account import models

def user_detail(request):
    user = models.CustomUser.objects.all()
    return {'user': user}