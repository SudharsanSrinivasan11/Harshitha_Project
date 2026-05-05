import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            row[1] = int(row[1])  
            row[2] = int(row[2])  
            row[3] = int(row[3])  
            data.append(row)
    return data

def peak_hour(data, area):
    max_count = -1
    peak_time = 0

    for i in data:
        if i[0].lower() == area.lower():
            if i[2] > max_count:
                max_count = i[2]
                peak_time = i[1]

    if max_count != -1:
        print("Peak hour:", peak_time, "with", max_count, "vehicles")
    else:
        print("Area not found")

def search_area(data, area):
    found = False
    for i in data:
        if i[0].lower() == area.lower():
            print(i)
            found = True
    if not found:
        print("No records found")

def average_speed(data, area):
    total = 0
    count = 0

    for i in data:
        if i[0].lower() == area.lower():
            total += i[3]
            count += 1

    if count > 0:
        print("Average speed:", total / count)
    else:
        print("Area not found")

def update_reason(data, area, time, new_reason):
    for i in data:
        if i[0].lower() == area.lower() and i[1] == time:
            i[4] = new_reason
            print("Updated successfully")
            return
    print("Record not found")

def congestion_level(count):
    if count < 70:
        return "Low"
    elif count < 120:
        return "Medium"
    else:
        return "High"

def show_congestion(data):
    for i in data:
        level = congestion_level(i[2])
        print(i[0], i[1], ":", level)


def reason_analysis(data):
    reasons = {}

    for i in data:
        r = i[4]
        if r in reasons:
            reasons[r] += 1
        else:
            reasons[r] = 1

    for r in reasons:
        print(r, ":", reasons[r])

def generate_report(data):
    max_count = -1
    max_area = ""

    for i in data:
        if i[2] > max_count:
            max_count = i[2]
            max_area = i[0]
    print("Most congested area:", max_area)

    reason_analysis(data)

data = load_data("traffic_data.csv")

while True:
    print("\n1. Peak Hour")
    print("2. Search Area")
    print("3. Average Speed")
    print("4. Update Reason")
    print("5. Show Congestion")
    print("6. Reason Analysis")
    print("7. Report")
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
