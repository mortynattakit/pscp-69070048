"""This code calculates how much energy u will get from milktea"""
def main():
    """The code starts here"""
    egg = input().split()
    eggtype = egg[0]
    egggram = float(egg[1])
    tea = input().split()
    teatype = tea[0]
    teasweetness = int(tea[1])
    teavolume = float(tea[2])
    match eggtype:
        case "H":
            eggcal = 5 * egggram
        case "O":
            eggcal = 3 * egggram
        case "J":
            eggcal = 2 * egggram
    teaprice =  {
        'R': {1:12,2:18,3:25},
        'T': {1:15,2:20,3:30},
        'M': {1:10,2:15,3:20}
    }
    result = (teaprice[teatype][teasweetness] * teavolume) + eggcal
    if result.is_integer():
        print(int(result))
    else:
        print(result)

main()
