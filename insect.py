import insectClass as i

def main():
        my_insect = i.Insect()
        my_insect.flight_length()

        print(f"Insect")
        print(f"Legs: {my_insect.legs}")
        print(f"Wings: {my_insect.wings}")
        print(f"Flight Length: {my_insect.get_flight()} miles")


main()