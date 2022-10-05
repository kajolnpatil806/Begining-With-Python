for i in range(1, 13):
    print("The no. {0} is squared as {1} and cubed as {2}."
          .format(i, i**2, i**3))
print()

print("String Formating: ")
for i in range(1, 13):
        print("The no. {0:2} is squared as {1:3} and cubed as {2:4}."
              .format(i, i**2, i**3))
print()

print("Inline Arrangements: ")
for i in range(1, 13):
    print("The no. {0:<2} is squared as {1:<3} and cubed as {2:<4}."
          .format(i, i**2, i**3))
print()

print("Centered Allignments: ")
for i in range(1, 13):
    print("The no. {0:^2} is squared as {1:^3} and cubed as {2:^4}."
          .format(i, i**2, i**3))
print()

print("Method 1: Pi is approximately {0:12}.".format(22 / 7))       # General Format and prints 15 default decimals
print("Method 2: Pi is approximately {0:3.12f}.".format(22 / 7))    #
print("Method 3: Pi is approximately {0:12.50f}.".format(22 / 7))
print("Method 4: Pi is approximately {0:52.50f}.".format(22 / 7))
print("Method 5: Pi is approximately {0:62.50f}.".format(22 / 7))
print("Method 6: Pi is approximately {0:72.50f}.".format(22 / 7))
print("Method 6: Pi is approximately {0:72.52f}.".format(22 / 7))
print("Method 7: Pi is approximately {0:73.51f}.".format(22 / 7))
print("Method 7: Pi is approximately {0:73.24f}.".format(22 / 7))
print("Method 8: Pi is approximately {0:70.54f}.".format(22 / 7))
print("Method 8: Pi is approximately {0:<70.54f}.".format(22 / 7))