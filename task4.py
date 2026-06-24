import base64

def protect_file(input_file, protected_file):
    try:
        with open(input_file, "rb") as file:
            data = file.read()

        encoded_data = base64.b64encode(data)

        with open(protected_file, "wb") as file:
            file.write(encoded_data)

        print("File protected successfully!")
        print("Protected file:", protected_file)

    except Exception as e:
        print("Error:", e)


def restore_file(protected_file, restored_file):
    try:
        with open(protected_file, "rb") as file:
            encoded_data = file.read()

        decoded_data = base64.b64decode(encoded_data)

        with open(restored_file, "wb") as file:
            file.write(decoded_data)

        print("File restored successfully!")
        print("Restored file:", restored_file)

    except Exception as e:
        print("Error:", e)


print("1. Protect File")
print("2. Restore File")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    input_file = input("Enter file name to protect: ")
    protected_file = input("Enter protected file name: ")
    protect_file(input_file, protected_file)

elif choice == "2":
    protected_file = input("Enter protected file name: ")
    restored_file = input("Enter restored file name: ")
    restore_file(protected_file, restored_file)

else:
    print("Invalid choice!")