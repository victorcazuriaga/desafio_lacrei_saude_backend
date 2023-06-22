from model_bakery.recipe import Recipe
from users.models import User

user_1 = Recipe(User, username = "victor", password ="123456")
user_2 = Recipe(User, username = "victor", password ="123456")
