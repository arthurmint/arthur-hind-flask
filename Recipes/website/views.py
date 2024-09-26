from flask import Blueprint, render_template, request, flash, session
import pandas as pd

views = Blueprint('views', __name__)
electronics = Blueprint('electronics', __name__)


"""
@views.route('/')
@views.route('/recipes')
def recipes():
    recipes = pd.read_csv('website/static/recipes.csv', header=None)
    return render_template("recipes.html", quizzes=recipes, listlength=len(recipes))
"""
@views.route('/')
def recipes():
    recipes = pd.read_csv('website/static/recipes.csv', header=None)

    print(recipes)

    """
    if str(sort) == "fastest":
    elif str(sort) == "slowest":
    elif str(sort) == "easiest":
    elif str(sort) =="hardest":
    
    if str(filter) == "veggie":
    if str(filter) == "stove":
    if str(filter) == "oven":
    """
    
    return render_template("recipes.html", quizzes=recipes, listlength=len(recipes))

@views.route('/recipes/<num>', methods=['GET'])
def practice(num: int):   
    if int(num) != 0:
        recipes = pd.read_csv('website/static/recipes.csv', header=None)
        ingredients = str(recipes[11][int(num)]).split(';')
        oven = False
        pan = False
        veggie = False
        if recipes[9][int(num)] == "y": 
            oven = True
        if recipes[10][int(num)] == "y":
            pan = True
        if recipes[12][int(num)] == "y":
            veggie = True
        return render_template("recipe.html", name=recipes[0][int(num)],
                               ingredients=ingredients,
                               listlength=len(ingredients),
                               pan=pan,
                               oven=oven,
                               veggie=veggie) 

    
    