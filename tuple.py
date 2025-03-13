from datetime import date
employees = [(101, "Asha", "HR"),
    (102, "bhanu", "IT"),
    (103, "Chinnu", "Finance"),
    (104, "arvind", "Marketing"),
]
attendance_records = []
def mark_attendance(emp_id, status):
    today = date.today().strftime("%Y-%m-%d")
    attendance_records.append((emp_id, today, status))
    print(f"Attendance marked: {emp_id} - {status}")
def search_attendance(emp_id):
    print(f"\nAttendance for Employee ID: {emp_id}")
    found = False
    for record in attendance_records:
        if record[0] == emp_id:
            print(f"Date: {record[1]}, Status: {record[2]}")
            found = True
    if not found:
        print("No attendance records found.")
def display_summary():
    print("\nAttendance Summary:")
    for emp in employees:
        emp_id = emp[0]
        present_days = sum(1 for rec in attendance_records if rec[0] == emp_id and rec[2] == "Present")
        absent_days = sum(1 for rec in attendance_records if rec[0] == emp_id and rec[2] == "Absent")
        print(f"{emp[1]} ({emp[2]}): Present: {present_days}, Absent: {absent_days}")
mark_attendance(101, "Present")
mark_attendance(102, "Absent")
mark_attendance(103, "Present")
mark_attendance(101, "Absent")
search_attendance(101)
display_summary()
