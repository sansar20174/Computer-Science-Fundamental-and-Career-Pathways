"""
Assigment no.1: Foundations of Computer Science & Computational Thinking
Assignment Title: Design and Simulate a Real-World Process using Flowcharts and Pseudocode
Topic: Hostel Mess Billing System
Author: Sansar Kumar
Programme: B. Tech CSE (Specialization in Full Stack Development)
Section: B
Roll no.: 2501350055
Course: Computer Science Fundamentals & Career Pathways
"""


def calculate_monthly_bill(student_name, meal_rate=50):
	"""Calculate the hostel mess bill for a student."""
	total_meals = 0
	days_in_month = 30

	print(f"\nHostel Mess Attendance for {student_name}")
	print("Enter number of meals taken each day (0 to 3):")

	for day in range(1, days_in_month + 1):
		while True:
			try:
				meals_today = int(input(f"Day {day}: "))
				if 0 <= meals_today <= 3:
					break
				else:
					print("Enter a number between 0 and 3.")
			except ValueError:
				print("Invalid input. Please enter a number.")
		total_meals += meals_today

	total_bill = total_meals * meal_rate

	print("\n==============================")
	print(f"Student: {student_name}")
	print(f"Total Meals: {total_meals}")
	print(f"Meal Rate: Rs.{meal_rate}")
	print(f"Total Bill: Rs.{total_bill}")
	print("==============================\n")

	return total_bill


# Example usage
if __name__ == "__main__":
	student_name = input("Enter student name: ")
	calculate_monthly_bill(student_name)
