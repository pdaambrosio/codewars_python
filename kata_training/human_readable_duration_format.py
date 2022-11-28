def format_duration(seconds: int) -> str:
    """
    It takes a number of seconds and returns a string of the format "X years, Y days, Z hours, etc."
    
    :param seconds: an integer representing the number of seconds to be formatted
    :type seconds: int
    :return: A string
    """
    if seconds == 0:
        return "now"
    time: dict = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1,
    }
    result: list = []
    for key, value in time.items():
        if seconds // value > 0:
            if seconds // value == 1:
                result.append(f"{seconds // value} {key}")
            else:
                result.append(f"{seconds // value} {key}s")
            seconds %= value
    if len(result) == 1:
        return result[0]
    return ", ".join(result[:-1]) + " and " + result[-1]


def main() -> None:
    print(format_duration(1))  # 1 second
    print(format_duration(62))  # 1 minute and 2 seconds
    print(format_duration(120))  # 2 minutes
    print(format_duration(3600))  # 1 hour
    print(format_duration(3662))  # 1 hour, 1 minute and 2 seconds
    

if __name__ == "__main__":
    main()
