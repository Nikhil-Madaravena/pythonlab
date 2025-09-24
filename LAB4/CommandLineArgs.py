import sys

# Print the script name
print("Script name:", sys.argv[0])

# Check if any arguments were passed
if len(sys.argv) > 1:
    print("Arguments passed:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("No arguments passed.")
