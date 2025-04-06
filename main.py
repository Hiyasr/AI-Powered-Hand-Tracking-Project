import os

def main():
    print("Choose a mode:")
    print("1. Virtual Mouse")
    print("2. Math Mode")
    print("3. ASL Recognition")
    print("4. Handwriting Recognition")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        os.system("python modules/VirtualMouse.py")
    elif choice == "2":
        os.system("python modules/MathMode.py")
    elif choice == "3":
        os.system("python modules/ASLRecognition.py")
    elif choice == "4":
        os.system("python modules/HandwritingRecognition.py")
    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
