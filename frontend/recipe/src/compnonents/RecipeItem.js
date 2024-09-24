import React from 'react';

const RecipeItem = ({ recipe }) => {
  return (
    <li>
      <h3>{recipe.name}</h3>
      <p>Ingredients: {recipe.ingredients.join(', ')}</p>
      <p>Instructions: {recipe.instructions}</p>
    </li>
  );
};

export default RecipeItem;
