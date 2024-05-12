def man(name, age, is_agree: bool):
    if is_agree:
        print(f"""
This man name is: {name}
This man age is: {age}""",
              end="")


_name = input("Please enter the name: ")
_age = input("Please enter the age: ")
question = input("Do you agree to print your details?[y/n]: ")
_is_agree = False
if question == "y":
    _is_agree = True
man(_name, _age, _is_agree)
