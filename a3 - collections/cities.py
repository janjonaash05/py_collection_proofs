if __name__ == "__main__":
    regions_cities_dict = \
        {"Zlinsky": ["Zlin"], "Stredocesky": ["Kladno", "Kutna Hora"], "Vysocina": ["Jihlava", "Telc"]}

    while True:
        print("Enter a region or a city")
        value = input()
        if value in regions_cities_dict.keys():
            print(f"Cities: {regions_cities_dict[value]}")
            break

        region_found = False
        for r in regions_cities_dict.keys():
            if value in regions_cities_dict[r]:
                print(f"Region: {r}")
                region_found = True
                break

        if region_found:
            break
        print("Error occurred, value is not in the dataset")


