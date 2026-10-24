# Each resource = [ID, name, category, quantity]
resources = [
    [101, "Laptop",     "Electronics", 8],
    [102, "Projector",  "Electronics", 0],
    [103, "Whiteboard", "Classroom",   5],
    [104, "Microphone", "Audio",       3],
    [105, "Camera",     "Electronics", 2],
]


def display_resources(resources):
    """Task 1: Display all resources with details."""
    if not resources:
        print("No resources available.")
        return
    print(f"{'ID':<6}{'Name':<15}{'Category':<15}{'Qty':<5}")
    print("-" * 41)
    for r in resources:
        print(f"{r[0]:<6}{r[1]:<15}{r[2]:<15}{r[3]:<5}")


def search_by_category(resources, category):
    """Task 2: Display all resources in a given category."""
    found = [r for r in resources if r[2].lower() == category.lower()]
    if not found:
        print(f"No resources found in category: {category}")
    else:
        print(f"Resources in '{category}':")
        for r in found:
            print(f"  {r[0]} | {r[1]} | Qty={r[3]}")


def find_unavailable(resources):
    """Task 3: Identify resources with zero quantity."""
    zero_qty = [r for r in resources if r[3] == 0]
    if not zero_qty:
        print("All resources are available.")
    else:
        print("Unavailable resources (qty = 0):")
        for r in zero_qty:
            print(f"  {r[0]} | {r[1]}")