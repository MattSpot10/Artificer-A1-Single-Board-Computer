import numpy as np




def e12_values(decade_low, decade_high):
    base_values = [
        1.0, 1.2, 1.5, 1.8, 2.2,
        2.7, 3.3, 3.9, 4.7, 5.6,
        6.8, 8.2, 10.0
    ]
    
    values = []
    for k in range(decade_low, decade_high):  # Adjust the range for how many decades you want
        for base in base_values:
            values.append(round(base * (10 ** k), 2))
    
    return values


def e24_values(decade_low, decade_high):
    base_values = [
        1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8,
        2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6,
        3.9, 4.7, 5.1, 5.6, 6.8, 8.2, 10,
        12, 15, 18, 22, 27, 30, 33, 39,
        43, 47, 51, 56, 62, 68, 75, 82,
        91, 100, 110, 120, 130, 150, 160,
        180, 200, 220, 240, 270, 300, 330,
        360, 390, 430, 470, 510, 560, 620,
        680, 750, 820, 910
    ]
    
    values = []
    for k in range(decade_low, decade_high):  # Adjust the range for how many decades you want
        for base in base_values:
            values.append(round(base * (10 ** k), 2))
    
    return values


def e48_values(decade_low, decade_high):
    base_values = [
        1.0, 1.05, 1.1, 1.15, 1.2, 1.3, 1.4,
        1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
        3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1,
        5.6, 6.2, 6.8, 7.5, 8.2, 9.1, 10.0,
        12.0, 15.0, 18.0, 22.0, 27.0, 30.0,
        33.0, 39.0, 43.0, 47.0, 51.0, 56.0,
        62.0, 68.0, 75.0, 82.0, 91.0
    ]
    
    values = []
    for k in range(decade_low, decade_high):  # Adjust the range for how many decades you want
        for base in base_values:
            values.append(round(base * (10 ** k), 2))
    
    return values

Vin = 5
Vout = 1.2222
V_error = .01

R1_values = e24_values(0, 1);
R2_values = e24_values(0, 1);

potential_values = []


for R1 in R1_values:
    for R2 in R2_values:
        calculated_Vout = Vin * (R2/(R1+R2))
        if (abs(calculated_Vout - Vout) < V_error) :
            potential_values.append([R1, R2, calculated_Vout, Vout/(R2/(R1+R2))])





np.set_printoptions(suppress=True)
print(np.matrix(potential_values))




