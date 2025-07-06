# personal drone delivary costnestimator - year 2077
cost_per_kilometer = 2.50
cost_per_kg = 1.80
urgent_surcharge = 15.00
delivary_distance_km = float(input("Enter the delivary(in kilometer): "))
package_weight_kg = float(input("Enter the package weight (in kilograms): "))
urgent_input = input(" Do you need urgent delivary? (yes/no): ")
distance_cost = delivary_distance_km*cost_per_kilometer
weight_cost=package_weight_kg*cost_per_kg
base_delivary_cost=distance_cost+weight_cost
if urgent_input =="yes":
    final_estimated_cost= base_delivary_cost + urgent_surcharge
    urgent_message = "urgent delivary surcharge applied"
else:
    final_estimated_cost=base_delivary_cost
    urgent_message="no urgent surcharge"

print("\n===delivar cost estimate (2077)===")
print(f"ditance:{delivary_distance_km}km")
print(f"package weight:{package_weight_kg}kg")
print(f"distance cost:{distance_cost} credits")
print(f"weight cost:{weight_cost} credits")
print(f"base delivary cost:{base_delivary_cost} credits")
print(f"{urgent_message}")
print(f"final estimeted delivary cost:{final_estimated_cost} credits")

    
