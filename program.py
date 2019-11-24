import process_data as proc
import display as disp

def cmd_menu():
    command = select_type_inp(["Enter New Value", "Draw Graph", "Exit"])

    if (command == "Enter New Value"):
        enter_val()
    elif (command == "Draw Graph"):
        draw_graph()
    else:
        raise SystemExit

def draw_graph():
    type = select_type_inp(["Weekly", "Monthly", "Yearly", "Back"])
    type = type[0:len(type) - 2]
    if (type == "Back"):
        cmd_menu()
    else:
        file = select_type_inp(["Basic", "Deluxe", "Total", "Back"])
        if (file == "Back"):
            draw_graph()
        else:
            disp.draw(proc.calc_rev(file + ".txt", type), file, type)

def enter_val():
    command = select_type_inp(["Basic", "Deluxe", "Total", "Back"])
    if (command == "Back"):
        cmd_menu()
    else:
        type = command + ".txt"
        val = enter_val_inp()
        curr_date = datetime.today().strftime("%d/%m/%Y")
        conf = input("Enter " + val + " on " + curr_date +"? Type yes to confirm: ")

        if (conf == "yes"):
            with open(type, "a") as file:
                file.write("\n" + val)
                print("Value has been added.")
        else:
            print("Returning to menu")

        cmd_menu()

def select_type_inp(strings):
    valid_inp = False
    while (not valid_inp):
        for i in range(1, len(strings) + 1):
            print("[" + str(i) + "] " + strings[i - 1])
        command = input("Please Select: ")

        valid_commands = []
        for i in range(1, len(strings) + 1):
            valid_commands.append(str(i))
        if (command in valid_commands):
            valid_inp = True

    return strings[int(command) - 1]

def enter_val_inp():
    valid_inp = False
    while (not valid_inp):
        val = input("Enter Value: ")
        if (val.isdigit()):
            valid_inp = True
    return val

cmd_menu()
