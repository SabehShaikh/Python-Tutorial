# program to find out whether a student is
#  pass or fail, if it requres total 40%
#  and atleast 33% in each subject to pass.
#  assume 3 subjects and take marks as an 
# input fromn the user

sub1 = int(input("Enter the marks of the first subject: "))
sub2 = int(input("Enter the marks of the second subject: "))
sub3 = int(input("Enter the marks of the third subject: "))

total_percentage = (sub1+sub2+sub3) / 300 * 100
print("The total percentage is: ", total_percentage)

if (total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You have passed the exam.")

else:
    print("You have failed the exam.")