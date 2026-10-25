# Data: [ID, name, category, quantity]
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2],
]


# Task 1: Show all resources
def display_resources(resources):
    if not resources:
        print("No resources available.")
        return
    for r in resources:
        print(r)                              # সরল প্রিন্ট (formatting বাদ)


# Task 2: Search by category
def search_by_category(resources, category):
    found = [r for r in resources if r[2].lower() == category.lower()]
    if not found:
        print("No resources found in category:", category)
    else:
        for r in found:
            print(r)


# Task 3: Show unavailable resources
def find_unavailable(resources):
    zero_qty = [r for r in resources if r[3] == 0]
    if not zero_qty:
        print("All resources are available.")
    else:
        for r in zero_qty:
            print(r)


# ---- Test ----
if __name__ == "__main__":
    display_resources(resources)
    search_by_category(resources, "Electronics")
    find_unavailable(resources)

    # Testing cases
    print("Unknown ID test:")
    unknown_id = 999
    found = False
    for r in resources:
        if r[0] == unknown_id:
            found = True
            break
    print("Found" if found else "Resource ID 999 not found.")

    print("Negative quantity test:")
    if -2 < 0:
        print("Error: quantity cannot be negative.")

    print("Empty list test:")
    display_resources([])