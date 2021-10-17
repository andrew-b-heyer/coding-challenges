# assumes that all words begin with one-nine

amount_dict = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "10": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 17, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
    "million": 1000000
}


def calculate_amounts(word_list):
    total = 0
    negative = False

    if word_list[0] == "negative":
        negative = True
        word_list.pop(0)

    # print(word_list)

    i = 0
    while i < len(word_list):
        word = word_list[i]

        # print("key to get: " + word)
        current_value = amount_dict.get(word)

        if current_value is None:
            raise ValueError("Invalid word entered: " + str(word))

        # check to see if there is a modifier word after the current one. If so, multiply them and add to total
        if i + 1 < len(word_list):
            modifier_value = amount_dict.get(word_list[i + 1])
            # print("modifier found: " + str(modifier_value))
            total += add_or_multiply(current_value, modifier_value)

            if i + 2 < len(word_list):
                # print("More to go, continuing")
                i = i + 2
            else:
                break

        # no modifiers found, so we simply add the value
        else:
            total += current_value
            i += 1

        # print("current value: " + str(current_value))
        # print("total is now " + str(total))

    if negative:
        return total * -1
    return total


def words_to_list(words):
    word_list = []

    for word in words:
        word_list.append(word.split())

    return word_list


def add_or_multiply(value1, value2):
    # print("figuring out what to do with: " + str(value1) + " " + str(value2))

    if value2 == 100 or value2 == 1000 or value2 == 1000000:
        return value1 * value2
    else:
        return value1 + value2


if __name__ == '__main__':

    words = ["six", "negative seven hundred twenty nine", "one million one hundred one", "three thousand forty one"]
    words_list = words_to_list(words)
    for word_list in words_list:
        print(calculate_amounts(word_list))
