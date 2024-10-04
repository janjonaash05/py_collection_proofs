
rivers_confluences_dict = \
    {
        "Sazava": ("Cikhaj", ["Davle", "Vltava", False]),
        "Vltava": ("Kvilda", ["Melnik", "Labe", False]),
        "Labe": ("Spindleruv Mlyn", ["Hradec Kralove", "Orlice", True]),
        "Dedina": ("Olesnice", ["Trebechovice", "Orlice", False]),
        "Otava": ("Relstejn", ["Zvikov", "Vltava", False]),
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
            if rivers_confluences_dict[river][1][1] not in rivers:
                rivers.append(rivers_confluences_dict[river][1][1])
                rivers.append(river)

        if city == rivers_confluences_dict[river][0]:
            rivers.append(river)
    return rivers


# returns origin (if any) and immediate confluence cities
def get_cities_by_river(river):
    cities = set()
    if river in rivers_confluences_dict.keys():
        cities.add(rivers_confluences_dict[river][0])
        cities.add(rivers_confluences_dict[river][1][0])

    for r in rivers_confluences_dict.keys():
        if river == rivers_confluences_dict[r][1][1]:
            cities.add(rivers_confluences_dict[r][1][0])
    return cities


# deletes after a failed attempt
transfers = []

# persistent
used_cities = set()
used_rivers = set()


def find_path(origin_city, target_city):
    if origin_city == target_city:
        return 1

    global transfers, used_rivers, used_cities
    used_cities.add(origin_city)

    rivers = set(get_rivers_by_city(origin_city))

    local_transfers = []
    river_cities_pairs = []

    for river in rivers:
        if river not in used_rivers:
            river_cities_pairs.append((river, get_cities_by_river(river)))
            local_transfers.append((origin_city, river))

    transfers.extend(local_transfers)
    if (len(rivers) == 1 and len(rivers.difference(used_rivers)) == 0) or all(e in used_cities for e in river_cities_pairs[0]):
        used_rivers.union(rivers)
        transfers = list(filter(lambda e: e not in local_transfers, transfers))
        return 0

    used_rivers = used_rivers.union(rivers)

    exit_sum = 0
    for pair in river_cities_pairs:
        (river, cities) = pair
        if target_city in cities:
            return 1

        for city in cities:
            if city not in used_cities and city != origin_city:
                exit_code = find_path(city, target_city)
                exit_sum += exit_code
        if exit_sum == 0:
            transfers.remove((origin_city, river))

    if exit_sum == 0:
        transfers = list(filter(lambda e: e not in local_transfers, transfers))
        return 0
    else:
        return 1


def main():
    while True:
        print("Enter the start city")
        start_city = input()
        print("Enter the target city")
        target_city = input()

        if not validate_city(start_city):
            print("Error occurred. Start city is not in the dataset")
            continue

        if not validate_city(target_city):
            print("Error occurred. Target city is not in the dataset")
            continue

        exit_code = find_path(start_city, target_city)
        if exit_code == 0:
            print("no path")
        elif exit_code == 1:
            for i in range(len(transfers)):
                print(f"{transfers[i][0]} via {transfers[i][1]} to {transfers[i+1][0] if i<len(transfers)-1 else target_city}")
        used_rivers.clear()
        used_cities.clear()
        transfers.clear()

if __name__ == "__main__":
    main()
