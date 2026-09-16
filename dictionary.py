# 1. Defining the dictionary
student = {
    "name": "Jiban",
        "age": 17,
            "city": "Kalapathar",
                "roll_number": 20
                }

                # 2. Printing the type of the variable
                print(type(student))  # Output: <class 'dict'>

                # 3. Accessing a value using its key (Fixed: added quotes around "name")
                print(student["name"])  # Output: Jiban

                # 4. Printing the entire dictionary
                print(student)

                # 5. Updating an existing key's value
                student["city"] = "Jayramdaspatna"
                print(student)

                # 6. Adding a new key-value pair (Fixed: corrected 'paint' to 'print' and fixed the key)
                student["fav_sub"] = "Maths"
                print(student["fav_sub"])

                # 7. Removing an item using pop()
                student.pop("fav_sub")
                print(student)

                # 8. Printing all keys and values
                print(student.keys())    # Prints all keys
                print(student.values())  # Prints all values
                