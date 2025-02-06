#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    last_item = ordered_list[-1]  # Get the last item
    ordered_list.append(last_item + 1)  # Append the next value

def remove_items_from_list(ordered_list, items_to_remove):
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

if __name__ == '__main__':
    print(my_list)

    # Add three items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)

    # Print the list after adding items
    print(my_list)

    # Remove items from the list
    remove_items_from_list(my_list, [1, 5, 6])

    # Print the list after removing items
    print(my_list)
