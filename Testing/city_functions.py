def city_country(city, coutry, population=0):
    if population==0:
        return (city.title() + ", " + coutry.title())
    return (city.title() + ", " + coutry.title() + " - população " + str(population))

