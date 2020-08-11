from django.shortcuts import render, HttpResponseRedirect, reverse

from recipes.models import Recipe, Author
from recipes.forms import AddAuthorForm, AddRecipeForm

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

def add_recipe(request):
	if request.method == "POST":
		form = AddRecipeForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Recipe.objects.create(
				title=data.get('title'),
				author=data.get('author'),
				description=data.get('description'),
				time_required=data.get('time_required'),
				instructions=data.get('instructions'),
			)
			return HttpResponseRedirect(reverse("homepage"))

	form = AddRecipeForm()
	return render(request, "generic_form.html", {"form": form})

def add_author(request):
	if request.method == "POST":
		form = AddAuthorForm(request.POST)
		form.save()
		return HttpResponseRedirect(reverse("homepage"))

	form = AddAuthorForm()
	return render(request, "generic_form.html", {"form": form})