'''String-Based Attendance Tracker 
Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  '''


attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record:")
print(attendance)

# 1. Count Present and Absent days
present_days = 0
absent_days = 0

for ch in attendance:
    if ch == 'P':
        present_days = present_days + 1
    elif ch == 'A':
        absent_days = absent_days + 1

print()
print("Present Days:", present_days)
print("Absent Days:", absent_days)


# 2. Calculate attendance percentage
total_days = len(attendance)

attendance_percentage = (present_days / total_days) * 100

print()
print("Attendance Percentage:", round(attendance_percentage, 2), "%")


# 3. Find longest consecutive streak of Presence
current_present_streak = 0
longest_present_streak = 0

for ch in attendance:
    if ch == 'P':
        current_present_streak = current_present_streak + 1

        if current_present_streak > longest_present_streak:
            longest_present_streak = current_present_streak

    else:
        current_present_streak = 0


# 4. Find longest consecutive streak of Absence
current_absent_streak = 0
longest_absent_streak = 0

for ch in attendance:
    if ch == 'A':
        current_absent_streak = current_absent_streak + 1

        if current_absent_streak > longest_absent_streak:
            longest_absent_streak = current_absent_streak

    else:
        current_absent_streak = 0


print()
print("Longest Present Streak:", longest_present_streak)
print("Longest Absent Streak:", longest_absent_streak)


# 5. Determine whether attendance is below 75%
print()

if attendance_percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: 75% or Above")


'''
Sample Output 
Attendance Record: 
PPAPPPAAPPPPAPP 
 
Present Days: 11 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Longest Present Streak: 4 
Longest Absent Streak: 2 
 
Attendance Status: Below 75%
