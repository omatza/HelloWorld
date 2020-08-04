# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#<<<<<<< HEAD   (the code I put in the master branch)
#    print_hi('master PyCharm')
#||||||| fe20b46 (the code in the parent commit)
    print_hi('PyCharm')
#======= (the code in the branch we merge from)
#    print_hi('my PyCharm')
#>>>>>>> featureA

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
