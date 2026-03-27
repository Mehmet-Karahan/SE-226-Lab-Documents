
users_list = {}
users_num = int(input("Enter number of users: "))

for i in range(users_num):
    user_name = input("Enter username: ")
    items_num = int(input(f"How many items?: "))

    items = []
    for j in range(items_num):
        item = input(f"item {j+1}:")
        items.append(item)

    users_list[user_name] = items

print("\nUSER DATA: ")
all_items_list = []
for user, items in users_list.items():
    print(f"{user} -> {items}")
    all_items_list.extend(items)

unique_all_items = set(all_items_list)

common_items = []
unique_item = []
item_counts = {}

for item in all_items_list:
    item_counts[item] = item_counts.get(item, 0) +1

for item, count in item_counts.items():
    if count > 1:
        common_items.append(item)
    else:
        unique_item.append(item)

print("\nCOMMON ITEMS: ")
for item in common_items:
    print(item)

print("\nUNIQUE ITEMS: ")
for item in unique_item:
    print(item)

if item_counts:
    max_count = max(item_counts.values())
    most_popular = [item for item, count in item_counts.items() if count == max_count]

    print("\nMOST POPULAR ITEM: ")
    for item in most_popular:
        print(item)

