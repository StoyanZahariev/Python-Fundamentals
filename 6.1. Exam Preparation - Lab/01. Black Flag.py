# Pirates invades

days_of_pirating = int(input())
plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_pirating + 1):
    total_plunder += plunder
    if day % 3 == 0:
        total_plunder += 0.5 * plunder
    if day % 5 == 0:
        total_plunder -= 0.3 * total_plunder

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    diff_percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {diff_percentage:.2f}% of the plunder.")


# each third day add 50% to the plunder
# each fifth day lose 30% from the plunder
