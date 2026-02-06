############### Approach 1 ###############

# Get input Separately

name = input("Please enter your name")
age = input("Please enter your age")

# validate using conditions

if age.isdigit():
  age = int(age)
  current_year = 2026
  birth_year = current_year - age

  print(f"""Whassup {name}! 
        I heard you were born in year {birth_year}.
        Anyways! Let me stop being creepy!
        Welcome to University of Maryland!
  """)
else:
  print('Please enter valid age')

############### Approach 2 ###############

name, age = input("Please enter your name and age separated by space: ").split()
# validate using try, except (Exception Handling)
try:
  age = int(age)
  current_year = 2026
  birth_year = current_year - age

  print(f"""Whassup {name}! 
        I heard you were born in year {birth_year}.
        Anyways! Let me stop being creepy!
        Welcome to University of Maryland!
  """)
except ValueError:
  print('Please provide valid age')