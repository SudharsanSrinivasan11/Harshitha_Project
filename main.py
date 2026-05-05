import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['vehicle_count'] = int(row['vehicle_count'])
            row['avg_speed'] = int(row['avg_speed'])
            row['time'] = int(row['time'])
            data.append(row)
    return data


def peak_hour(data, area):
    max_count = -1
    peak_time = None
    for row in data:
        if row['area'].lower() == area.lower():
            if row['vehicle_count'] > max_count:
                max_count = row['vehicle_count']
                peak_time = row['time']
    if peak_time is not None:
        print(f"Peak hour in {area} is {peak_time}:00 with {max_count} vehicles")
    else:
        print("Area not found")



def search_area(data, area):
    found = False
    for row in data:
        if row['area'].lower() == area.lower():
            print(row)
            found = True
    if not found:
        print("No records found")


def average_speed(data, area):
    total = 0
    count = 0
    for row in data:
        if row['area'].lower() == area.lower():
            total += row['avg_speed']
            count += 1
    if count > 0:
        print(f"Average speed in {area}: {total / count:.2f} km/h")
    else:
        print("Area not found")


def update_reason(data, area, time, new_reason):
    for row in data:
        if row['area'].lower() == area.lower() and row['time'] == time:
            row['reason'] = new_reason
            print("Updated successfully")
            return
    print("Record not found")


def congestion_level(vehicle_count):
    if vehicle_count < 70:
        return "Low"
    elif vehicle_count < 120:
        return "Medium"
    else:
        return "High"


def show_congestion(data):
    for row in data:
        level = congestion_level(row['vehicle_count'])
        print(f"{row['area']} at {row['time']}:00 → {level}")



def reason_analysis(data):
    reasons = {}
    for row in data:
        r = row['reason']
        reasons[r] = reasons.get(r, 0) + 1
    for k, v in reasons.items():
        print(f"{k}: {v} times")


def generate_report(data):
    max_area = ""
    max_count = -1

    for row in data:
        if row['vehicle_count'] > max_count:
            max_count = row['vehicle_count']
            max_area = row['area']

    print("\n--- Traffic Report ---")
    print(f"Most congested area: {max_area} ({max_count} vehicles)")

    reason_analysis(data)


data = load_data("traffic_data.csv")

while True:
    print("\n1. Peak Hour")
    print("2. Search Area")
    print("3. Average Speed")
    print("4. Update Reason")
    print("5. Show Congestion")
    print("6. Reason Analysis")
    print("7. Generate Report")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        area = input("Enter area: ")
        peak_hour(data, area)

    elif choice == 2:
        area = input("Enter area: ")
        search_area(data, area)

    elif choice == 3:
        area = input("Enter area: ")
        average_speed(data, area)

    elif choice == 4:
        area = input("Enter area: ")
        time = int(input("Enter time: "))
        reason = input("Enter new reason: ")
        update_reason(data, area, time, reason)

    elif choice == 5:
        show_congestion(data)

    elif choice == 6:
        reason_analysis(data)

    elif choice == 7:
        generate_report(data)

    elif choice == 8:
        break

    else:
        print("Invalid choice")
