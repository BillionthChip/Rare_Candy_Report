import requests

def main():

    userinput = input("Enter a name of a pokemon to see their stats: \n")
 
    url = f"https://pokeapi.co/api/v2/pokemon/{userinput.lower()}"

    response = requests.get(url)

    data = response.json()

    print(" ")

    name = data["name"]
    display = print("Name:\n" + name.title())
    print(" ")


    weight = data["weight"]
    displayW = print("Weight: " + str(weight))
    print(" ")


    height = data["height"]
    displayH = print("Height: "+ str(height))
    print(" ")

    abilities = data["abilities"]
    first_ability = abilities[0]
    first_ability1 = first_ability["ability"]["name"]

    print("Ability #1: " + first_ability1.title())
    print(" ")

    abilities = data["abilities"]
    second_ability = abilities[1]
    second_ability2 = first_ability["ability"]["name"]

    print("Ability #2: " + second_ability2.title())
    print(" ")


    moves = data["moves"]
    moves_list = moves[0]
    moves_list1 = moves_list["move"]["name"]
    print("Move #1: " + moves_list1.title())
    
    print(" ")

    moves = data["moves"]
    moves_list = moves[1]
    moves_list1 = moves_list["move"]["name"] 
    print("Move #2: " + moves_list1.title())

    print(" ")

    id = data["id"]
    print("Pokemon ID: " + str(id))

    image = data["sprites"]["front_default"]
    
    print(f"Image of {userinput}: " + image)


print("Welcome To Poke-Stats!\n")



main()