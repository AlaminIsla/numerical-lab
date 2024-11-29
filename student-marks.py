import numpy as np

# Step 1: Create a 6x4 matrix "allMarks"
allMarks = np.array([
    [24, 44, 36, 36],  # Amit
    [52, 57, 68, 76],  # Bhavna
    [66, 53, 69, 73],  # Chetan
    [85, 40, 86, 72],  # Deepak
    [15, 47, 25, 28],  # Elizabeth
    [79, 72, 82, 91]   # Farah
])

# Step 2: Scale down all marks by 20
scaledMarks = allMarks / 20
print("Scaled Marks:\n", scaledMarks)

# Step 3: Extract Chetan's marks and calculate his total
chetanMarks = allMarks[2]  # 2nd index corresponds to Chetan
chetanTotal = np.sum(chetanMarks)
print("\nChetan's Marks:", chetanMarks)
print("Chetan's Total Marks:", chetanTotal)

# Step 4: Calculate the average marks for Thermodynamics and Mechanics
thermo_avg = np.mean(allMarks[:, 2])  # 2nd column for Thermodynamics
mech_avg = np.mean(allMarks[:, 3])   # 3rd column for Mechanics
print("\nAverage Marks in Thermodynamics:", thermo_avg)
print("Average Marks in Mechanics:", mech_avg)
