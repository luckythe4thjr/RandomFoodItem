import sqlite3
import random

con = sqlite3.connect('foods.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS foods(food, category)")


def category(cat_initial):
    if cat_initial == 'b':
        breakfast = 'Breakfast'
        return breakfast
    elif cat_initial == 'l':
        lunch = 'Lunch'
        return lunch
    elif cat_initial == 'd':
        dinner = 'Dinner'
        return dinner
    elif cat_initial == 's':
        snack = 'Snack'
        return snack
    else:
        error = '!'
        return error


def hasItem():
    res = cur.execute("SELECT food FROM foods")
    return res.fetchone()


def addItem(food_item, food_cat):
    cur.execute("INSERT INTO foods(food, category) VALUES(?, ?)", (food_item, food_cat))
    con.commit()


def addMore():
    while True:
        add_food = input('What food do you wish to add? ').title()
        while True:
            food_category = input(f'{add_food} is (B) Breakfast, (L) Lunch, (D) Dinner, or (S) Snack: ')
            if category(food_category) == '!':
                print('Invalid answer.')
            else:
                break
        addItem(add_food, category(food_category))

        add_additional = input('Do you wish to add another (Y/N)? ').lower()
        if add_additional == 'y':
            pass
        else:
            break

    foods = []
    for item in cur.execute("SELECT food FROM foods"):
        foods.append(item)
    print(random.choice(foods))
    return


if hasItem() is None:
    insert_food = input('What food do you wish to add? ').title()
    while True:
        insert_category = input(f'{insert_food} is (B) Breakfast, (L) Lunch, (D) Dinner, or (S) Snack: ').lower()
        if category(insert_category) == '!':
            print('Invalid answer.')
        else:
            addItem(insert_food, category(insert_category))
            break
    add_more = input('Do you wish to add more (Y/N)? ')
    addMore()

else:
    see_prior = input('Wish to see previously added? ').lower()
    if see_prior == 'y':
        for row in cur.execute("SELECT food FROM foods"):
            print(row)
            add_more = input('Do you wish to add more (Y/N)? ').lower()
            if add_more == 'y':
                addMore()
            else:
                pass
    else:
        pass

con.close()