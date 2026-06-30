"""
=========================================================
        PASSWORD STRENGTH CHECKER MODULE
=========================================================
Description:
Evaluates the strength of a password based on:
- Length
- Uppercase letters
- Lowercase letters
- Digits
- Special characters
- Entropy Calculation
=========================================================
"""

import math
import re


def calculate_entropy(password):
    """Calculate password entropy."""

    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26

    if re.search(r"[A-Z]", password):
        pool += 26

    if re.search(r"\d", password):
        pool += 10

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


def evaluate_password(password):
    """
    Evaluate password strength.

    Returns:
        dict
    """

    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Increase password length to 12 or more.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    # Symbols
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    # Determine strength
    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    elif score == 5:
        strength = "Strong"

    else:
        strength = "Very Strong"

    entropy = calculate_entropy(password)

    return {
        "strength": strength,
        "score": min(score, 5),
        "entropy": entropy,
        "suggestions": suggestions
    }


if __name__ == "__main__":

    pwd = input("Enter Password: ")

    result = evaluate_password(pwd)

    print("\nPassword Analysis")
    print("----------------------------")
    print("Strength :", result["strength"])
    print("Score    :", result["score"], "/5")
    print("Entropy  :", result["entropy"], "bits")

    if result["suggestions"]:
        print("\nSuggestions:")
        for item in result["suggestions"]:
            print("-", item)
    else:
        print("\nExcellent Password!")