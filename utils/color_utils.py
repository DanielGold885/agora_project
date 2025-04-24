import re

def is_red_border(rgb_string):
    import re

    match = re.match(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", rgb_string)
    if not match:
        return False

    r, g, b = map(int, match.groups())
    # Flexibly match reddish tones (like Bootstrap 5.3 danger border shades)
    return r > 180 and g < 140 and b < 140
