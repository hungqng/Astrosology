def get_astrological_sign(month, day):
    """Returns the astrological sign based on the given month and day."""
    if month == 1:
        if day <= 19:
            return "Capricorn"
        else:
            return "Aquarius"
    elif month == 2:
        if day > 29:
            return "Invalid"
        elif day <= 18:
            return "Aquarius"
        elif day <= 29:
            return "Pisces"
        else:
            return "Invalid"
    elif month == 3:
        if day <= 20:
            return "Pisces"
        else:
            return "Aries"
    elif month == 4:
        if day <= 19:
            return "Aries"
        else:
            return "Taurus"
    elif month == 5:
        if day <= 20:
            return "Taurus"
        else:
            return "Gemini"
    elif month == 6:
        if day <= 20:
            return "Gemini"
        else:
            return "Cancer"
    elif month == 7:
        if day <= 22:
            return "Cancer"
        else:
            return "Leo"
    elif month == 8:
        if day <= 22:
            return "Leo"
        else:
            return "Virgo"
    elif month == 9:
        if day <= 22:
            return "Virgo"
        else:
            return "Libra"
    elif month == 10:
        if day <= 22:
            return "Libra"
        else:
            return "Scorpio"
    elif month == 11:
        if day <= 21:
            return "Scorpio"
        else:
            return "Sagittarius"
    elif month == 12:
        if day <= 21:
            return "Sagittarius"
        else:
            return "Capricorn"
    else:
        return "Invalid"

def get_compatible_signs(sign):
    """Return a list of compatible astrological signs for a given sign."""
    if sign == "Aries":
        return ["Leo", "Sagittarius", "Gemini", "Aquarius"]
    elif sign == "Taurus":
        return ["Virgo", "Capricorn", "Cancer", "Pisces"]
    elif sign == "Gemini":
        return ["Libra", "Aquarius", "Aries", "Leo"]
    elif sign == "Cancer":
        return ["Scorpio", "Pisces", "Taurus", "Virgo"]
    elif sign == "Leo":
        return ["Sagittarius", "Aries", "Gemini", "Libra"]
    elif sign == "Virgo":
        return ["Capricorn", "Taurus", "Cancer", "Scorpio"]
    elif sign == "Libra":
        return ["Aquarius", "Gemini", "Leo", "Sagittarius"]
    elif sign == "Scorpio":
        return ["Pisces", "Cancer", "Virgo", "Capricorn"]
    elif sign == "Sagittarius":
        return ["Aries", "Leo", "Libra", "Aquarius"]
    elif sign == "Capricorn":
        return ["Taurus", "Virgo", "Scorpio", "Pisces"]
    elif sign == "Aquarius":
        return ["Gemini", "Libra", "Sagittarius", "Aries"]
    elif sign == "Pisces":
        return ["Cancer", "Scorpio", "Capricorn", "Taurus"]
    else:
        return []

def main():
    """Main function that prompts the user for input and displays their astrological sign and compatible signs."""
    # Get user input
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))
    
    # Get astrological sign
    sign = get_astrological_sign(month, day)

    # Print summary and compatible signs
    print("Your astrological sign is", sign)
    print("Summary:")
    if sign == "Aries":
        print("Aries are known for their leadership skills, independence, and passion.")
    elif sign == "Taurus":
        print("Taurus are known for their reliability, patience, and determination.")
    elif sign == "Gemini":
        print("Geminis are known for their adaptability, wit, and curiosity.")
    elif sign == "Cancer":
        print("Cancers are known for their emotional intelligence, loyalty, and creativity.")
    elif sign == "Leo":
        print("Leos are known for their confidence, generosity, and creativity.")
    elif sign == "Virgo":
        print("Virgos are known for their attention to detail, practicality, and loyalty.")
    elif sign == "Libra":
        print("Libras are known for their diplomacy, charm, and social skills.")
    elif sign == "Scorpio":
        print("Scorpios are known for their passion, intensity, and loyalty.")
    elif sign == "Sagittarius":
        print("Sagittariuses are known for their adventurous spirit, optimism, and honesty.")
    elif sign == "Capricorn":
        print("Capricorns are known for their determination, responsibility, and ambition.")
    elif sign == "Aquarius":
        print("Aquariuses are known for their independence, originality, and humanitarianism.")
    elif sign == "Pisces":
        print("Pisces are known for their intuition, empathy, and creativity.")
    else:
        print("Invalid date entered.")

    # Get and print compatible signs
    compatible_signs = get_compatible_signs(sign)
    if compatible_signs:
        print("Compatible signs: ", end="")
        print(*compatible_signs, sep=", ")
    else:
        print("No compatible signs found.")
main()
