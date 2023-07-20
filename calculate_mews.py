def calculate_mews(hr, rr, sbp, temp, loc):
    mews = 0
    
    # Calculate Heart Rate Score
    if hr >= 130:
        mews += 3
    elif hr >= 110:
        mews += 2
    elif hr >= 100:
        mews += 1
    
    # Calculate Respiratory Rate Score
    if rr >= 30:
        mews += 3
    elif rr >= 21:
        mews += 2
    elif rr >= 9:
        mews += 1
    
    # Calculate Systolic Blood Pressure Score
    if sbp <= 70:
        mews += 2
    elif sbp <= 100:
        mews += 1
    
    # Calculate Body Temperature Score
    if temp >= 39:
        mews += 2
    elif temp >= 38:
        mews += 1
    
    # Calculate Level of Consciousness Score
    if loc < 15:
        mews += 3
    elif loc < 10:
        mews += 2
    elif loc < 13:
        mews += 1
    
    return mews

# Example usage
heart_rate = 120
respiratory_rate = 22
systolic_blood_pressure = 90
body_temperature = 37.5
level_of_consciousness = 14

mews_score = calculate_mews(
    heart_rate, respiratory_rate, systolic_blood_pressure,
    body_temperature, level_of_consciousness
)

print("MEWS Score:", mews_score)
