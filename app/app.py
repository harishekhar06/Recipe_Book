from flask import Flask, request, jsonify
from models import Recipe
from database import init_db
from utils import format_response, handle_error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

init_db(app)

# Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.get_all()
    return jsonify(format_response([recipe for recipe in recipes]))

# Add a recipe
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    try:
        data = request.get_json()
        recipe = Recipe(
            name=data['name'],
            ingredients=data['ingredients'],
            instructions=data['instructions']
        )
        recipe.save()
        return jsonify(format_response(None, "Recipe added successfully")), 201
    except Exception as e:
        return jsonify(handle_error(str(e))), 400

# Get a recipe by ID
@app.route('/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.get_by_id(recipe_id)
    if recipe:
        return jsonify(format_response(recipe))
    return jsonify(handle_error("Recipe not found")), 404

# Delete a recipe by ID
@app.route('/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    result = Recipe.delete_by_id(recipe_id)
    if result.deleted_count > 0:
        return jsonify(format_response(None, "Recipe deleted successfully"))
    return jsonify(handle_error("Recipe not found")), 404

if __name__ == '__main__':
    app.run(debug=True)
