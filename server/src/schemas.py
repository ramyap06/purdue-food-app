from pydantic import BaseModel

# create an object schema corresponding to each table in the database
class ItemsBase(BaseModel):
    item_id: int
    name: str
    calories: int
    protein: int
    carbs: int
    fats: int
    dining_hall_id: int

class DiningHallInfoBase(BaseModel):
    dining_hall_id: int
    name: str
    location: str

class NutritionalGoalsBase(BaseModel):
    nutritional_goal_id: int
    name: str

class UsersBase(BaseModel):
    user_id: int
    name: str
    weight_lbs: int
    height_in: int
    meal_plan: int
    curr_loc: str
    nutritional_goal_id: int

class MealLogBase(BaseModel):
    meal_log_id: int
    date_time: str
    user_id: int
    dining_hall_id: int
    item_id: int
    nutritional_goal_id: int