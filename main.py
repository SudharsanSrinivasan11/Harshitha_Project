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

def show_all(data):
    for i in data:
        print(i)

def peak_hour(data, area):
    maximum = -1
    peak = 0
    for i in data:
        if i[0].lower() == area.lower():
            if i[2] > maximum:
                maximum = i[2]
                peak = i[1]
    if maximum == -1:
        print("Area not found")
    else:
        print("Peak hour in", area, "is", peak)
        print("Vehicle count:", maximum)

def search_area(data, area):
    found = False
    for i in data:
        if i[0].lower() == area.lower():
            print(i)
            found = True
    if found == False:
        print("No record found")

def average_speed(data, area):
    total = 0
    count = 0
    for i in data:
        if i[0].lower() == area.lower():
            total = total + i[3]
            count = count + 1
    if count == 0:
        print("Area not found")
    else:
        avg = total / count
        print("Average speed:", avg)

def update_reason(data, area, time, reason):
    found = False
    for i in data:
        if i[0].lower() == area.lower() and i[1] == time:
            i[4] = reason
            found = True
            print("Reason updated")
    if found == False:
        print("Record not found")

def update_vehicle(data, area, time, value):
    found = False
    for i in data:
        if i[0].lower() == area.lower() and i[1] == time:
            i[2] = value
            found = True
            print("Vehicle count updated")
    if found == False:
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
        print(i[0], i[1], level)

def reason_analysis(data):
    regular = 0
    peak = 0
    accident = 0
    construction = 0
    for i in data:
        if i[4].lower() == "regular":
            regular = regular + 1
        elif i[4].lower() == "peak":
            peak = peak + 1
        elif i[4].lower() == "accident":
            accident = accident + 1
        elif i[4].lower() == "construction":
            construction = construction + 1
    print("Regular:", regular)
    print("Peak:", peak)
    print("Accident:", accident)
    print("Construction:", construction)

def generate_report(data):
    maximum = -1
    area = ""
    for i in data:
        if i[2] > maximum:
            maximum = i[2]
            area = i[0]
    print("Traffic Report")
    print("Most congested area:", area)
    print("Highest vehicle count:", maximum)
    reason_analysis(data)

def save_data(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            "area",
            "time",
            "vehicle_count",
            "avg_speed",
            "reason"
        ])
        for i in data:
            writer.writerow(i)

    print("File saved")

def add_record(data):
    area = input("Enter area: ")
    time = int(input("Enter time: "))
    vehicles = int(input("Enter vehicle count: "))
    speed = int(input("Enter average speed: "))
    reason = input("Enter reason: ")
    row = [area, time, vehicles, speed, reason]
    data.append(row)
    print("Record added")

def delete_record(data, area, time):
    found = False
    for i in data:
        if i[0].lower() == area.lower() and i[1] == time:
            data.remove(i)
            found = True
            print("Record deleted")
            break
    if found == False:
        print("Record not found")

data = load_data("traffic_data.csv")
while True:
    print()
    print("1. Show all records")
    print("2. Peak hour analysis")
    print("3. Search by area")
    print("4. Average speed")
    print("5. Update reason")
    print("6. Update vehicle count")
    print("7. Show congestion")
    print("8. Reason analysis")
    print("9. Generate report")
    print("10. Add record")
    print("11. Delete record")
    print("12. Save file")
    print("13. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        show_all(data)
    elif choice == 2:
        area = input("Enter area: ")
        peak_hour(data, area)
    elif choice == 3:
        area = input("Enter area: ")
        search_area(data, area)
    elif choice == 4:
        area = input("Enter area: ")
        average_speed(data, area)
    elif choice == 5:
        area = input("Enter area: ")
        time = int(input("Enter time: "))
        reason = input("Enter new reason: ")
        update_reason(data, area, time, reason)
    elif choice == 6:
        area = input("Enter area: ")
        time = int(input("Enter time: "))
        value = int(input("Enter new vehicle count: "))
        update_vehicle(data, area, time, value)
    elif choice == 7:
        show_congestion(data)
    elif choice == 8:
        reason_analysis(data)
    elif choice == 9:
        generate_report(data)
    elif choice == 10:
        add_record(data)
    elif choice == 11:
        area = input("Enter area: ")
        time = int(input("Enter time: "))
        delete_record(data, area, time)
    elif choice == 12:
        save_data("traffic_data.csv", data)
    elif choice == 13:
        print("Program ended")
        break
    else:
        print("Invalid choice")
