def calculate_severity(area_percentage):

    if area_percentage < 10:
        score = 30
        severity = "LOW"

    elif area_percentage < 25:
        score = 60
        severity = "MEDIUM"

    else:
        score = 90
        severity = "HIGH"

    return score, severity