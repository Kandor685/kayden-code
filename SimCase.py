def switch_case(option):
    cases = {
        1: "Option 1 Selected", 
        2: "Option 2 Selected",
        3: "Option 3 Selected"
    }
    return cases.get(option, "Invalid option")

print(switch_case(5))