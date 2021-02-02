breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Ramen", "Soups"]
dinners = ["Steak", "Salad", "Pasta"]

#print(type(zip(breakfast, lunch, dinner)))
#print(list(zip(breakfast, lunch, dinner)))

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meal for today was {breakfast} and {lunch} and {dinner}.")