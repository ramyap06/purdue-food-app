import psycopg2
import itertools
from menu_items import menu_items

DATABASE_URL = "postgresql://postgres:ramyap06@localhost:5432/food_app"

class ItemsObj:
    id_iter = itertools.count()
    def __init__(self, name='NOT NECESSARY', dining_hall_id=-1, calories=100, protein=100, carbs=100, fats=100):
        self.id = next(self.id_iter)
        self.name = name
        self.dining_hall_id = dining_hall_id
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats

    def unpack(self):
        query_list = [self.id, self.name, self.dining_hall_id, self.calories, self.protein, self.carbs, self.fats]
        print(query_list)
        return query_list


# array of objects to create
item_objects = [
    ItemsObj("Grilled Cheese with Garlic Butter", 0, 547, 22, 42, 36),
    ItemsObj("California Dreaming Sandwich", 0, 530, 29, 38, 28),
    ItemsObj("Spicy Club", 0, 430, 30, 41, 16),
    ItemsObj("Veggie Wrap", 0, 431, 15, 53, 18),
    ItemsObj("Chicken Bacon Ranch Wrap", 0, 637, 40, 55, 27),
    ItemsObj("Italian Sub", 0, 701, 37, 54, 38),
    ItemsObj("Turkey Sub", 0, 605, 40, 48, 28),
    ItemsObj("Double Egg Everything Bagel", 0, 521, 24, 52, 26),
    ItemsObj("Double Egg Plain Bagel", 0, 764, 24, 52, 25),
    ItemsObj("Strawberry Granola Parfait", 0, 265, 14, 41, 6),
    ItemsObj("Chicken Caesar Salad", 0, 530, 19, 19, 43),
    ItemsObj("Chef Salad", 0, 490, 23, 12, 39),
    ItemsObj("Garden Salad", 0, 320, 7, 13, 28),
    ItemsObj("Peanut Butter and Jelly Crunch Sandwich", 0, 750, 27, 79, 40),
    ItemsObj("Nutella Berry Crunch Sandwich", 0, 764, 22, 95, 32),
]

def post(item_objects: list[ItemsObj]):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO items(id, name, dining_hall_id, calories, protein, carbs, fats) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        for i in item_objects:
            cursor.execute(postgres_insert_query, i.unpack())
            connection.commit()
            count = cursor.rowcount
        print(count, "Record inserted successfully \
        into items table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into items table", error)

    finally:
        # closing database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get(object: ItemsObj):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        postgres_select_query = "SELECT * FROM items WHERE id = %s"
        cursor.execute(postgres_select_query, str(object.id))
        items_records = cursor.fetchall()
        print("Selecting rows from items table using cursor.fetchall")
        print("Print each row and it's columns values")
        for row in items_records:
            print("id = ", row[0], )
            print("name = ", row[1])
            print("dining_hall_id  = ", row[2])
            print("calories  = ", row[3])
            print("protein  = ", row[4])
            print("carbs  = ", row[5])
            print("fats  = ", row[6], "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_all():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        postgres_select_query = "SELECT * FROM items"
        cursor.execute(postgres_select_query)
        print("Selecting rows from items table using cursor.fetchall")
        items_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in items_records:
            print("id = ", row[0], )
            print("name = ", row[1])
            print("dining_hall_id  = ", row[2])
            print("calories  = ", row[3])
            print("protein  = ", row[4])
            print("carbs  = ", row[5])
            print("fats  = ", row[6], "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
import psycopg2


def put(object: ItemsObj):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Update single record now
        sql_update_query = """UPDATE items
                             SET name = %s, dining_hall_id = %s, calories = %s, protein = %s, carbs = %s, fats = %s 
                            WHERE id = %s"""
        cursor.execute(sql_update_query, (object.name, object.dining_hall_id, object.calories, object.protein, object.carbs, object.fats, object.id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def delete(object: ItemsObj):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """DELETE FROM items
                            WHERE id = %s"""
        cursor.execute(sql_delete_query, str(object.id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def delete_all():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        # Update single record now
        sql_delete_query = """DELETE FROM items"""
        cursor.execute(sql_delete_query)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

post(item_objects=item_objects)