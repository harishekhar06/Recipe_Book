from bson.objectid import ObjectId
from database import db

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def save_to_db(self):
        return db.recipes.insert_one(self.to_dict())

    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

    @staticmethod
    def get_all():
        return list(db.recipes.find())

    @staticmethod
    def get_by_id(recipe_id):
        return db.recipes.find_one({"_id": ObjectId(recipe_id)})

    @staticmethod
    def delete_by_id(recipe_id):
        return db.recipes.delete_one({"_id": ObjectId(recipe_id)})
