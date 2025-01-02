def determine_type(input_value):
    if input_value.isdigit():
        return "Integer"
    try:
        float_value = float(input_value)
        if '.' in input_value:
            return "Float"
        else:
            return "Integer"
    except ValueError:
        return "String"

check = input("Enter the variable : ")
print(determine_type(check))
