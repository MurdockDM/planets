planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

twoNewPlanets = ("Earth", "Mars")

planet_list.extend(twoNewPlanets)

planet_list.insert(4, "Venus")

planet_list.append("Pluto")

rocky_planets = planet_list[:1]

rocky_planets.extend(planet_list[4:7])

del(planet_list[-1])