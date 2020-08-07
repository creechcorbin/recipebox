from django.shortcuts import render

from homepage.models import Recipe, Author

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