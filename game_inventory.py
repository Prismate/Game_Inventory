def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for item, count in inventory.items():
        print(f"{item}: {count}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] == 0:
                del inventory[item]


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    inventory = {'rope': 1, 'torch': 6, 'blanket': 3}

    item_title = "item name"
    count_title = "count"
    separator = " | "
    dash_char = '-'
    test = [len(str(item)) for item in inventory.keys()]

    max_width_item = max([len(str(item)) for item in inventory.keys()] + [len(item_title)])
    max_width_count = max([len(str(count)) for count in inventory.values()] + [len(count_title)])
    horizontal_line = dash_char * (max_width_item + max_width_count + len(separator))

    # header
    print(horizontal_line)
    print(f"{item_title:>{max_width_item}}{separator}{count_title:>{max_width_count}}")
    print(horizontal_line)

    # rows
    inventory_items = []
    if order == "count,asc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=False)
    elif order == "count,desc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=True)
    else:
        inventory_items = inventory.items()

    for item, count in inventory_items:
        print(f"{item:>{max_width_item}}{separator}{count:>{max_width_count}}")

    # footer
    print(horizontal_line)


def import_inventory(inventory, filename="import_inventory.csv"):
    """Import new inventory items from a CSV file."""

    try:
        with open(filename) as file:
            for line in file:
                items_to_add = line.split(',')
                add_to_inventory(inventory, items_to_add)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename="export_inventory.csv"):
    """Export the inventory into a CSV file."""

    outputs = []

    for item, count in inventory.items():
        for i in range(count):
            outputs.append(item)

    outputs_with_commas = ','.join(outputs)

    try:
        with open(filename, "w") as file:
            file.write(outputs_with_commas)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")


expected_output = \
"""rope: 1
torch: 6"""

_inventory = {'rope': 1, 'torch': 6, 'blanket': 3}
test = [str(item) for item in _inventory.keys()]

print(f"{'item_title':>{20}}{'|'}{'count_title':>{15}}")



print(test)
