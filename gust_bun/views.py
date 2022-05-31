from django.shortcuts import render
# from ml import gust_bun_model_cuv_v4_1 as glhf


def index(request):
    """HOME PAGE"""
    recipe = {"recipe_title": "Mighty Recipe Title", "recipe_ingredients": ["100 x fun", "lots of cereals."]}
    if request.method == "POST":
        # recipe = glhf.get_new_recipe()
        print(recipe)
    return render(request, 'index.html', recipe)

# def get_new_recipe():
#     # Generate recipe and return it
#     recipe = {"recipe_title": "Alakazam", "recipe_ingredients": ["1/4 x egg", "6 tomatoe"]}
#     return recipe