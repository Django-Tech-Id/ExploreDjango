from datetime import datetime
from django.shortcuts import render, redirect

import category
from .models import Category
from .form import CategoryForm
import uuid

# Create your views here.
def dashboardCategory(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category.html', context)

def dashboardCategoryCreate(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            # form.created_by = request.user.id
            # print('coba')
            # print(request.user.id)
            # print('coba')
            # status = 1
            # if request.POST['status'] == 'on':
            #     status = 1
            # else:
            #     status = 0

            # create = Category.objects.create(
            #     name = request.POST['name'],
            #     description = request.POST['description'],
            #     status = status,
            #     # image = request.FILES['image'],
            #     created_by = request.user
            #     # created_at = strftime(datetime.now()),
            # )
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            # form.save(request.user.id)
            return redirect('dashboard-category')
    context = {'form': form}
    return render(request, 'category/category_form.html', context)

def dashboardCategoryEdit(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            print('coba')
            print(request.user.id)
            print('coba')
            create = Category.objects.create(
                id = uuid.uuid4,
                name = request.POST['name'],
                description = request.POST['description'],
                status = request.POST['status'],
                image = request.FILES['image']['name'],
                created_by = request.user.id,
                created_at = datetime.now(),
            )
            # form.instance.created_by = request.user.id
            # # form.created_by = request.user.id
            # form.save()
            return redirect('dashboard-category')
    context = {'form': form}
    return render(request, 'category/category_form.html', context)

def dashboardCategoryDelete(request, id):
    category = Category.objects.get(id=id)
    category.image.delete(save=True)
    category.delete()

    return redirect('dashboard-category')