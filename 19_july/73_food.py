def manage_fav_foods():
    foods = {}
    for i in range(1, 5):
        foods[i] = input(f"Enter favourite food #{i}: ")

    print("\nYour favourite foods:")
    for k, v in foods.items():
        print(f"{k}: {v}")

    remove = input("\nEnter the food you want to remove: ")

    # Remove the food
    for key in list(foods):
        if foods[key].lower() == remove.lower():
            del foods[key]
            break

    # Sort and re-index
    sorted_foods = sorted(foods.values())
    new_foods = {i+1: sorted_foods[i] for i in range(len(sorted_foods))}

    print("\nUpdated food list:")
    for k, v in new_foods.items():
        print(f"{k}: {v}")

# Call the function
manage_fav_foods()
