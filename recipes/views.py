from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipes.models import Recipe, Author
from recipes.forms import AddAuthorForm, AddRecipeForm, LoginForm

def index_view(request):
	my_recipes = Recipe.objects.all()
	return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "WELCOME TO THE DUDE'S DELICACIES "})

def post_detail(request, post_id):
	my_recipe = Recipe.objects.filter(id=post_id).first()
	return render(request, "post_detail.html", {"post": my_recipe})

def author_detail(request, author_id):
	my_author = Author.objects.filter(id=author_id).first()
	authored_recipes = Recipe.objects.filter(author=my_author)
	return render(request, "author_detail.html", {"author": my_author, "recipes": authored_recipes})

@login_required
def add_recipe(request):
	if request.method == "POST":
		form = AddRecipeForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Recipe.objects.create(
				title=data.get('title'),
				author=request.user.author,
				description=data.get('description'),
				time_required=data.get('time_required'),
				instructions=data.get('instructions'),
			)
			return HttpResponseRedirect(reverse("homepage"))

	form = AddRecipeForm()
	return render(request, "generic_form.html", {"form": form})

@login_required
def add_author(request):
	if request.user.is_staff:
		if request.method == "POST":
			form = AddAuthorForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
				login(request, new_user)
			return HttpResponseRedirect(reverse("homepage"))

		form = AddAuthorForm()
		return render(request, "generic_form.html", {"form": form})
	else:
		return HttpResponseForbidden("This aggression will not stand, man.")

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data.get("username"), password=data.get("password"))
			if user:
				login(request, user)
				# return HttpResponseRedirect(reverse("homepage"))
				return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
	
	form = LoginForm()
	return render(request, "generic_form.html", {"form":form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("homepage"))

# def signup_view(request):
# 	if request.method == "POST":
# 		form = AddAuthorForm(request.POST)
# 		if form.is_valid():
# 			data = form.cleaned_data
# 			new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
# 			login(request, new_user)
# 			return HttpResponseRedirect(reverse("homepage"))

# 	form = AddAuthorForm()
# 	return render(request, "generic_form.html", {"form": form})
