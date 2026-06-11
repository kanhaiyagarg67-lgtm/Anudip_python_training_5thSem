'''Problem 2: Hospital Patient Record Management System 
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.  '''


# patient data
patients = [
    "P101,Anuj,Normal",
    "P102,Rahul,Critical",
    "P103,Priya,Stable",
    "P104,Neha,Critical",
    "P105,Amit,Stable",
    "P106,Sneha,Normal",
    "P107,Karan,Critical",
    "P108,Pooja,Stable",
    "P109,Rohit,Normal",
    "P110,Anjali,Stable"
]

# Display all patient records.  
with open("patients.txt", "w") as file:
    for patient in patients:
        file.write(patient + "\n")

normal = stable = critical = 0

print("All Patient Records:")
with open("patients.txt", "r") as file:
    for line in file:
        print(line.strip())
print("----------------------------------")

# Display critical patients.
# Count patients under each status.  
print("\nCritical Patients:")

with open("patients.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        pid = data[0]
        name = data[1]
        status = data[2]

        if status == "Normal":
            normal += 1
        elif status == "Stable":
            stable += 1
        elif status == "Critical":
            critical += 1
            print(name) # print the name of all critical patient

print("\nPatient Count:")
print("Normal:", normal)
print("Stable:", stable)
print("Critical:", critical)
print("-------------------------------")

# Search patient details using Patient ID.

search_id = input("Enter Patient ID to search: ")

found = False

with open("patients.txt", "r") as file:
    for line in file:
        if line.startswith(search_id):
            print("Patient Found:")
            print(line.strip())
            found = True

if found == False:
    print("Patient not found")
print("---------------------------------")

#Save critical patient records to critical_patients.txt.  

with open("patients.txt", "r") as file:
    with open("critical_patients.txt", "w") as critical_file:
        for line in file:
            data = line.strip().split(",")
            if data[2] == "Critical":
                critical_file.write(line)

print("Critical Patient Report Generated Successfully.")

'''
Sample Output 
Critical Patients: 
Rahul 
Neha 
Karan 
 
Patient Count: 
Normal : 3 
Stable : 4 
Critical : 3 
 
Patient Found: 
P104,Neha,Critical 
 
Critical Patient Report Generated Successfully.'''
