# A tiling contractor calculates cost per tile for each job.
# If zero tiles are entered by mistake, the program should not crash.

def cost_per_tile(total_cost, num_tiles):
    try:
        result = total_cost / num_tiles
    except ZeroDivisionError:
        print("Cannot divide: zero tiles entered.")
    else:
        print(f"KES {total_cost} / {num_tiles} tiles = KES {result:.2f} per tile")
    finally:
        print("(Calculation attempted)")
    print()

cost_per_tile(45000, 300)
cost_per_tile(30000, 0)
cost_per_tile(62400, 480)