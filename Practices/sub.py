def count_substring(string, sub_string):
    i = string.find(sub_string)
    while i != -1:
        i = string.find(sub_string, i + len(sub_string), len(string))
    return string.count(sub_string)


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
