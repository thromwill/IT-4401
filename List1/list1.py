#list1


foods = ['pizza', 'salad', 'hamburger', 'steak', 'apple', 'orange'];

def display_list(label, items):
    print(label)
    for i in items:
        print(i)


display_list("foods in original order:", foods)

foods.sort()
display_list("foods in ascending alphabetical order:", foods)

foods.sort(reverse = True)
display_list("foods in descending alphabetical order:", foods)

foods2= sorted(foods)
display_list("foods2 in ascending alphabetical order:", foods2)

display_list("foods still in descending alphabetical order:", foods)

foods.reverse()
display_list("foods in ascending alphabetical order:", foods)

foods.append('carrots')
foods.append('milk')
display_list("sorted foods with carrots and milk appended to end:", foods)

foods.sort()
display_list("foods in descending alphabetical order:", foods)

pizzaIndex = foods.index('pizza')
print("Pizza is at", pizzaIndex)

foods.insert(pizzaIndex, 'fries')
pizzaIndex = foods.index('pizza')
print("Pizza is now at", pizzaIndex)

