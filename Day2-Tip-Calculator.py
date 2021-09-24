print("Welcome to my tip calculator")
bill = float(input("What was the total bill?\n$"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people will spilt the bill?\n"))


total = percent / 100 * bill + bill

total_per_person = total / people

#Formats the code to provide 2 decimal places
final_round = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${final_round}")