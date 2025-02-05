# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Declaring numbers
num1 = 10
num2 = 20

# Adding the numbers
sum_result = add(num1, num2)

# Displaying the result
print("The sum is:", sum_result)

# Testing function
def test_add():
    assert add(1, 4) == 5
    assert add(1, -2) == -1

# Run the test
test_add()
print("All tests passed successfully!")
