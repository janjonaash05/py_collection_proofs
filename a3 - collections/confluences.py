rivers_confluences_dict = \
    {
        "Sazava": ("Cikhaj", ["Davle", "Vltava", False]),
        "Vltava": ("Kvilda na Sumave", ["Melnik", "Labe", False]),
        "Labe": ("Spindleruv Mlyn", ["Hradec Kralove", "Orlice", True]),
        "Dedina": ("Olesnice v Orlickych horach", ["Trebechovice pod Orebem", "Orlice", False]),
        "Otava": ("Rejstejn na Sumave", ["Zvikov", "Vltava", False]),
    }
# False - ends, True - continues


def validate_city(city):
    for r in rivers_confluences_dict:
        if city in rivers_confluences_dict[r][1]:
            return True
        elif city == rivers_confluences_dict[r][0]:
            return True
    return False


# returns primary (continuing) and secondary (ending) rivers
def get_rivers_by_city(city):
    rivers = []

    for river in rivers_confluences_dict:
        if city in rivers_confluences_dict[river][1]:
            rivers.append(rivers_confluences_dict[river][1][1])
        elif city == rivers_confluences_dict[river][0]:
            rivers.append(river)
    return rivers


# returns origin (if any) and immediate confluence cities
def get_cities_by_river(river):
    cities = [None]
    confluence_cities = []
    if river in rivers_confluences_dict.keys():
        cities[0] = (rivers_confluences_dict[river][0])
        confluence_cities.append(rivers_confluences_dict[river][1][0])

    for r in rivers_confluences_dict.keys():
        if river == rivers_confluences_dict[r][1][1]:
            confluence_cities.append(rivers_confluences_dict[r][1][0])
    cities.append(confluence_cities)
    return cities


transfers = [[None, "Melnik", "Labe"],["Labe", "Hradec", "Orlice"]]
used_cities = {}


def find_path(target_city, origin_city):
    rivers = get_rivers_by_city(origin_city) + get_rivers_by_city(target_city)
    river_cities_pairs = []
    for river in rivers:
        river_cities_pairs.append((river, get_cities_by_river(river)))

    for pair in river_cities_pairs:
        print(pair)
        if (origin_city == pair[1][0] and target_city in pair[1][1]) or (target_city == pair[1][0] and origin_city in pair[1][1]) or (target_city in pair[1][1] and origin_city in pair[1][1]):
            print(f"{origin_city} via {pair[0]} to {target_city}")
            return

    for pair in river_cities_pairs:
        pass


def main():
    while True:
        print("Enter the start city")
        start_city = input()
        print("Enter the target city")
        target_city = input()

        find_path(target_city, start_city)

        if not validate_city(start_city):
            print("Error occurred. Start city is not in the dataset")
            continue

        if not validate_city(target_city):
            print("Error occurred. Target city is not in the dataset")
            continue


if __name__ == "__main__":
    main()
