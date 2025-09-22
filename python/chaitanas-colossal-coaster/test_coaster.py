#!/usr/bin/env python3

from list_methods import (
    add_me_to_the_queue,
    find_my_friend,
    add_me_with_my_friends,
    remove_the_mean_person,
    how_many_namefellows,
    remove_the_last_person,
    sorted_names
)

# Test all functions
print("Testing Chaitana's Colossal Coaster Functions:")
print()

# Test add_me_to_the_queue
print("1. add_me_to_the_queue:")
express_queue = ['Tony', 'Bruce']
normal_queue = ['RobotGuy', 'WW']
result = add_me_to_the_queue(express_queue, normal_queue, 0, 'HawkEye')
print(f"   add_me_to_the_queue({express_queue}, {normal_queue}, 0, 'HawkEye') -> {result}")
print(f"   Updated queues: express={express_queue}, normal={normal_queue}")
print()

# Test find_my_friend
print("2. find_my_friend:")
queue = ['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket']
result = find_my_friend(queue, 'Natasha')
print(f"   find_my_friend({queue}, 'Natasha') -> {result}")
print()

# Test add_me_with_my_friends
print("3. add_me_with_my_friends:")
queue = ['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket']
result = add_me_with_my_friends(queue, 0, 'Bucky')
print(f"   add_me_with_my_friends({queue}, 0, 'Bucky') -> {result}")
print()

# Test remove_the_mean_person
print("4. remove_the_mean_person:")
queue = ['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket']
result = remove_the_mean_person(queue, 'Ultron')
print(f"   remove_the_mean_person({queue}, 'Ultron') -> {result}")
print()

# Test how_many_namefellows
print("5. how_many_namefellows:")
queue = ['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket']
result = how_many_namefellows(queue, 'Natasha')
print(f"   how_many_namefellows({queue}, 'Natasha') -> {result}")
print()

# Test remove_the_last_person
print("6. remove_the_last_person:")
queue = ['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket']
result = remove_the_last_person(queue)
print(f"   remove_the_last_person({queue}) -> '{result}'")
print()

# Test sorted_names
print("7. sorted_names:")
queue = ['Steve', 'Ultron', 'Natasha', 'Rocket']
result = sorted_names(queue)
print(f"   sorted_names({queue}) -> {result}")
print(f"   Original queue unchanged: {queue}")

print()
print("All tests completed!")
