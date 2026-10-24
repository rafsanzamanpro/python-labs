# ============================================
# Lab 05 - Exercise 1: Campus Resource Tracker
# File: resource_tracker.py
# ============================================

# Each resource = [ID, name, category, available_quantity]
resources = [
    [101, "Laptop",     "Electronics", 8],
    [102, "Projector",  "Electronics", 0],
    [103, "Whiteboard", "Classroom",   5],
    [104, "Microphone", "Audio",       3],
    [105, "Camera",     "Electronics", 2],
]


# -------- Task 1 --------
def display_resources(resources):
    """Display all resources with their details."""
    if not resources:
        print("No resources available.")
        return

    print(f"{'ID':<6}{'Name':<15}{'Category':<15}{'Qty':<5}")
    print("-" * 41)
    for r in resources:
        print(f"{r[0]:<6}{r[1]:<15}{r[2]:<15}{r[3]:<5}")


# -------- Task 2 --------
def search_by_category(resources, category):
    """Display all resources belonging to a given category."""
    found = [r for r in resources if r[2].lower() == category.lower()]
    if not found:
        print(f"No resources found in category: {category}")
    else:
        print(f"Resources in '{category}':")
        for r in found:
            print(f"  {r[0]} | {r[1]} | Qty={r[3]}")


# -------- Task 3 --------
def find_unavailable(resources):
    """Identify resources whose available quantity is zero."""
    zero_qty = [r for r in resources if r[3] == 0]
    if not zero_qty:
        print("All resources are available.")
    else:
        print("Unavailable resources (qty = 0):")
        for r in zero_qty:
            print(f"  {r[0]} | {r[1]}")


# -------- Optional (for testing invalid data) --------
def add_resource(resources, rid, name, category, qty):
    """Add a resource but reject negative quantity."""
    if qty < 0:
        print("Error: quantity cannot be negative.")
        return
    resources.append([rid, name, category, qty])


# -------- Main / Testing --------
if __name__ == "__main__":
    print("=== All Resources ===")
    display_resources(resources)

    print("\n=== Search: Electronics ===")
    search_by_category(resources, "Electronics")

    print("\n=== Unavailable Resources ===")
    find_unavailable(resources)

    # ----- Testing & Debugging cases -----
    print("\n=== Testing & Debugging ===")

    # 1. Unknown category
    print("\n[Test] Unknown category 'Furniture':")
    search_by_category(resources, "Furniture")

    # 2. Negative quantity
    print("\n[Test] Adding resource with negative quantity:")
    add_resource(resources, 106, "Tablet", "Electronics", -2)

    # 3. Resource with zero units (already present, but show)
    print("\n[Test] Zero-quantity check again:")
    find_unavailable(resources)

    # 4. Empty resource list
    print("\n[Test] Empty resource list:")
    display_resources([])