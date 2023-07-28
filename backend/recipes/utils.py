import io


class RecipeTXTCreator:
    '''Класс для создания списка покупок'''
    file_name = 'ingredients.txt'

    def __init__(self, recipes):
        self.recipes = recipes

    def create(self):
        '''создание файла для получения общего количества ингредиентов
           и создания списка покупок'''
        ingredients_count = self._get_ingredients_amount()
        file = self._create_ingredients_file(ingredients_count)
        return file

    def _get_ingredients_amount(self):
        ingredients_amount = {}
        for recipe in self.recipes:
            ingredients_amount = self._add_recipe_ingredients(
                recipe,
                ingredients_amount)
        return ingredients_amount

    @staticmethod
    def _add_recipe_ingredients(recipe, ingredients_amount):
        '''создаем словарь интгредиентов, учитывая их количество'''
        for ingredient_in_recipe in recipe.ingredient_list.all():
            ingredient = ingredient_in_recipe.ingredient
            amount = ingredient_in_recipe.amount
            ingredients_amount[ingredient] = ingredients_amount.setdefault(ingredient, 0) + amount

        return ingredients_amount

    @staticmethod
    def _create_ingredients_file(ingredients_amount):
        '''записываем ингредиенты и их количество в файл'''
        file = io.StringIO()
        for ingredient, amount in ingredients_amount.items():
            file.write(f'{ingredient.name} - {amount} {ingredient.unit_of_measurement}\n')
        file.seek(0)
        return file
