# noinspection SpellCheckingInspection

if __name__ == "__main__":
    rivers_cities_dict = \
        {
            "Labe": ("Labska louka", ["Hradec Kralove", "Pardubice", "Kolin"]),
            "Vltava": ("Kvilda na Sumave", ["Praha", "Krumlov", "Ceske Budejovice"]),
            "Berounka": ("Plzen", ["Beroun", "Cernosice", "Praha"])
        }

    while True:
        print("Enter a city or a river")
        value = input()
        if value in rivers_cities_dict.keys():
            print(f"Source: {rivers_cities_dict[value][0]}, Goes through: {rivers_cities_dict[value][1]}")
            break

        rivers = []
        for r in rivers_cities_dict.keys():
            if value == rivers_cities_dict[r][0] or value in rivers_cities_dict[r][1]:
                rivers.append(r)

        if len(rivers) == 0:
            print("Error occurred, value is not in the dataset")
            continue

        print(f"Rivers: {rivers}")
        break


