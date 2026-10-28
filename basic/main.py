from operator import truediv


def is_even(number):
    """ Return True if number is even and False if it is odd.

    :param number:
    :return:
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text):
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: THe text to check
    :return: The number of voewels
    """
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count += 1

    return count



def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

      :param celsius: The temperature in Celsius.
    :return: The temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def reverse_text(text):
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: The text to reverse
    :return: Reversed text
    """
    return text[::-1]


def larger_number(a, b):
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:The firts number
    :param b: The second number
    :return: THe larger of the two numbers
    """
    if a > b:
        return a
    else:
        return b




def average_two(a, b):
    """Calculate and return the average of two integers.

 :param a: The first number.
    :param b: The second number.
    :return: The average of the two numbers.:
    """
    return (a + b) / 2


def can_afford(balance, cost):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    pass


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

       :param balance: The amount of money available.
    :param cost: The price of the item.
    :return: True if you can afford it, otherwise False.
    """
    return balance >= cost


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: THe sentence eto search.
    :param word: THe word to look for
    :return: True if the word is found, otherwise false
    """
    return word in sentence


def calculate_tip(cost, percent):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

       :param cost: The ORiginal cost.
    :param percent: The tip percentage.
    :return: The amount of the tip.
    """
    return cost * percent / 100


def make_initials(first_name, last_name):
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

     :param first_name: The person's first name.
    :param last_name: The person's last name.
    :return: The uppercase initials of both Names.
    """
    return first_name[0].upper() + last_name[0].upper()


def percent_score(points, possible):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points earned.
    :param possible: The total points possible.
    :return: The percentage earned, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    return points / possible * 100


def is_between(number, minimum, maximum):
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

     :param number: The number to check.
    :param minimum: The lowest allowed value.
    :param maximum: The highest allowed value.
    :return: True if the number is within the range, otherwise False.
    """
    return minimum <= number <= maximum


def all_different(a, b, c):
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

 :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if all three strings are different, otherwise False.
    """
    return a != b and a != c and b != c


def average_three(a, b, c):
    """Calculate and return the average of three integers.

      :param a: The first number.
    :param b: The second number.
    :param c: The third number.
    :return: The average of the three numbers.
    """
    return (a + b + c) / 3


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

     :param temperature: The temperature to check.
    :param cold_limit: The temperature limit for cold.
    :param hot_limit: The temperature limit for hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    print(is_even(4))
    print(count_vowels("Hello"))
    print(celsius_to_fahrenheit(0))
    print(reverse_text("Helene Tchemawe"))
    print(larger_number(5, 8))
    print(average_two(4, 6))
    print(can_afford(20, 15))
    print(repeat_text("Helene the queen!", 67))
    print(contains_word("hello world", "world"))
    print(calculate_tip(20, 15))
    print(make_initials("Helene", "Queen"))
    print(percent_score(18, 20))
    print(is_between(5, 1, 10))
    print(all_different("C", "B", "A"))
    print(average_three(1, 6, 5))
    print(describe_temperature(22, 60, 5))
