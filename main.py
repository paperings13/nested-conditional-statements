print("Exam Eligibility Check")
answer = input(" Do you have a medical cause ? (Y for yes and N for No) ")
if answer == "Y" or answer == "y":
    print("You are eligible for the exam ")
else:
    attendance = int(input("Enter your attendance "))
    if attendance > 75 :
        print(" You are eligible for the exam")
    else:
        print("You are not eligible for this exam")
    