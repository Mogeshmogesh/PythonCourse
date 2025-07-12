plant1 = ("Lettuce", "Leafy")
plant2 = ("Tomato", "Fruit")
plant3 = ("Spinach", "Leafy")
farm_stats = {"Rooftop-A": {"plants": [plant1, plant2], "growth": "Good"},"Rooftop-B": {"plants": [plant3], "growth": "Average"} }
zones={"Rooftop-A","Rooftop-B"}
species={plant1[0],plant2[0],plant3[0]}
for zone in farm_stats:
    print("\nFarm Zone:", zone)
    print("Growth Status:",
farm_stats [zone] ["growth"])
print("Plants:")
for plant in farm_stats [zone]["plants"]:
    print( plant [0], " Type:",plant[1])
print("All plant species",species)
print("All farm zones:",zones)
