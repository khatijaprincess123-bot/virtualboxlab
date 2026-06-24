def analyze_email(email_text):
    risk_score = 0
    warnings = []

    suspicious_keywords = [
        "urgent",
        "verify your account",
        "click here",
        "password",
        "bank details",
        "ssn",
        "credit card",
        "immediately",
        "limited time",
        "winner"
    ]

    for keyword in suspicious_keywords:
        if keyword.lower() in email_text.lower():
            risk_score += 1
            warnings.append(f"Suspicious phrase detected: '{keyword}'")

    if "http://" in email_text or "https://" in email_text:
        risk_score += 1
        warnings.append("Contains a link. Verify the source before clicking.")

    if risk_score == 0:
        risk_level = "Safe"
    elif risk_score <= 2:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    print("\n=== Email Analysis Report ===")
    print("Risk Level:", risk_level)

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("No suspicious content detected.")

# User Input
print("Paste the email content below:")
email_content = input()

analyze_email(email_content)