middayTemps = []
midnightTemps = []
def main():

    for x in range(30):
        print(x + 1)
        print(f"Type Midday Temp for day {x+1}")
        print("Midday Temp: ")
        middayTemp = input()
        print("Midnight Temp: ")
        midnightTemp = input()
        middayTemps.append(middayTemp)
        midnightTemps.append(midnightTemp)

    print(len(middayTemps))
    print(len(midnightTemps))


main()
