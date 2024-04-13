"""
how many we can bake
"""

def cakes(recipe, available):
    """
    This function calculates the maximum number of cakes that can be made with the available ingredients.

    Args:
    recipe: A dictionary containing the ingredients required for one cake.
    available: A dictionary containing the available quantities of each ingredient.

    Returns:
    The maximum number of cakes that can be made.
    """
    return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)
