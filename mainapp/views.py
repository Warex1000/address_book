from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import Users


def index(request):
    if request.method == 'POST':
        new_user = UsersForm(request.POST, request.FILES or None)
        new_user.save()

    new_user = UsersForm()
    all_users = Users.objects.all()
    context = {'all_users': all_users, 'new_user': new_user}
    return render(request, 'mainapp/index.html', context)


def delete(request, user_id):
    user = Users.objects.get(pk=user_id)
    user.delete()

    return redirect('/')


def edit(request):
    users = Users.objects.all()
    all_users = []

    for user in users:
        users_info = dict(name=user.name, surname=user.surname, image=user.image)
        all_users.append(users_info)

    context = {'all_users': all_users}
    return render(request, 'mainapp/edit.html', context)


# def edit(request, users_id):
#     users_item = get_object_or_404(Users, pk=users_id)
#     return render(request, 'mainapp/edit.html', {"users_item ": users_item })


# def edit(request, user_id):
#
#     users = Users.objects.get(pk=user_id)
#     all_users = []
#
#     for user in users:
#         users_info = dict(name=user.name, surname=user.surname, image=user.image)
#         all_users.append(users_info)
#
#     context = {'all_users': all_users, 'user': users}
#     return render(request, 'mainapp/edit.html', context)


# def edite(self, *, object_list=None, **kwargs):
#     context = super().edite(**kwargs)
#     context['users'] = Users.objects.)
#     assert isinstance(context, Users.objects)
#     return Users.objects.filter(category_id=self.kwargs['users'])






