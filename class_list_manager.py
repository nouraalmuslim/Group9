# Class List Manager - Group 9
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: Noura (task 5)
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result

# ===== Each student adds her function ABOVE this line =====

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Uppercase names:", to_upper(names))

    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))

main()

