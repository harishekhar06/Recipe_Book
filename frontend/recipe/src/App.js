import React, { useState, useEffect } from 'react';
import AddRecipe from './components/AddRecipe';
import RecipeList from './components/RecipeList';

const App = () => {
  const [recipes, setRecipes] = useState([]);

  const fetchRecipes = async () => {
    try {
      const response = await fetch('/recipes');
      const data = await response.json();
      setRecipes(data); 
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };

  useEffect(() => {
    fetchRecipes();
  }, []);

  const handleAddRecipe = async (newRecipe) => {
    try {
      const response = await fetch('/add_recipe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newRecipe),
      });

      if (response.ok) {
        fetchRecipes(); // Refresh the list after adding a recipe
      } else {
        console.error('Failed to add recipe');
      }
    } catch (error) {
      console.error('Error adding recipe:', error);
    }
  };

  return (
    <div className="App">
      <h1>Recipe Book</h1>
      <AddRecipe onAddRecipe={handleAddRecipe} />
      <RecipeList recipes={recipes} />
    </div>
  );
};

export default App;
