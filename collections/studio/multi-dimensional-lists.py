food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = sorted(food.split(","))
equipment_cabinet = sorted(equipment.split(","))
pets_cabinet = sorted(pets.split(","))
sleep_aids_cabinet = sorted(sleep_aids.split(","))

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print("Cargo hold structure:", cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
print("#--------------------------------------------#")
print("Input a cabinet (0 - 3) in the cargo_hold")
cabinet_choice = int(input())

# d) Use bracket notation and format to display the contents of the selected cabinet. 
# If the user entered an invalid number, print an error message.
if 0 <= cabinet_choice < len(cargo_hold):
    print(f"Contents of the selected cabinet: {cargo_hold[cabinet_choice]}")
else:
    print("Error: Invalid cabinet number. Please enter a number between 0 and 3.")

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND 
# a particular item. Use the in method to check if the cabinet contains the 
# selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
print("#--------------------------------------------#")
print("Input a cabinet (0 - 3) in the cargo_hold")
cabinet_choice = int(input())
print("Input the item you want to check the cabinet for")
item_choice = str(input())
if 0 <= cabinet_choice < len(cargo_hold):
    if item_choice in cargo_hold[cabinet_choice]:
        print(f"Cabinet {cargo_hold[cabinet_choice]} DOES contain {item_choice}")
    else:
        print(f"Cabinet {cargo_hold[cabinet_choice]} does NOT contain {item_choice}")
else:
    print("Error: Invalid cabinet number. Please enter a number between 0 and 3.")