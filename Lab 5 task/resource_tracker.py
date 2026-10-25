

# Resource information: ID, name, category, quantity
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2],
]


# Show all available resources
def display_resources(resources):
    if not resources:
        print("No resources available.")
        return

    print(f"{'ID':<6}{'Name':<15}{'Category':<15}{'Qty':<5}")
    print("-" * 41)

    for r in resources:
        print(f"{r[0]:<6}{r[1]:<15}{r[2]:<15}{r[3]:<5}")


# Find resources by category
def search_by_category(resources, category):
    found = []

    for r in resources:
        if r[2].lower() == category.lower():
            found.append(r)

    if not found:
        print("No resources found in category:", category)
    else:
        print("Resources in", category + ":")
        for r in found:
            print(f"  {r[0]} | {r[1]} | Qty={r[3]}")


# Show resources that have zero quantity
def find_unavailable(resources):
    zero_qty = []

    for r in resources:
        if r[3] == 0:
            zero_qty.append(r)

    if not zero_qty:
        print("All resources are available.")
    else:
        print("Unavailable resources:")
        for r in zero_qty:
            print(f"  {r[0]} | {r[1]}")


# Add a resource if its quantity is valid
def add_resource(resources, rid, name, category, qty):
    if qty < 0:
        print("Error: quantity cannot be negative.")
        return

    resources.append([rid, name, category, qty])
    print("Resource added successfully.")


# Check whether a resource ID exists
def search_by_id(resources, rid):
    found = False

    for r in resources:
        if r[0] == rid:
            print(f"Resource found: {r[1]} | Qty={r[3]}")
            found = True
            break

    if not found:
        print("Resource ID not found.")


# Test the functions
if __name__ == "__main__":

    print("All Resources")
    display_resources(resources)

    print("\nSearch by Category")
    search_by_category(resources, "Electronics")

    print("\nUnavailable Resources")
    find_unavailable(resources)

    # Try a category that does not exist
    print("\nTesting unknown category")
    search_by_category(resources, "Furniture")

    # Try searching for an ID that does not exist
    print("\nTesting unknown resource ID")
    search_by_id(resources, 999)

    # Try adding a resource with a negative quantity
    print("\nTesting negative quantity")
    add_resource(resources, 106, "Tablet", "Electronics", -2)

    # Check the resource with zero quantity again
    print("\nTesting zero quantity")
    find_unavailable(resources)

    # Check what happens when the list is empty
    print("\nTesting empty resource list")
    display_resources([])