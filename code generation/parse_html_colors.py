PRESET_COLORS = {
    "red": "#FF0000",
    "limegreen": "#32CD32",
    "blue": "#0000FF"
}

def parse_html_color(color):
    if color.startswith('#'):
        if len(color) == 4:
            color = '#' + color[1]*2 + color[2]*2 + color[3]*2
        return {
            'r': int(color[1:3], 16),
            'g': int(color[3:5], 16),
            'b': int(color[5:7], 16)
        }
    else:
        color_dict = PRESET_COLORS.get(color.lower())
        if color_dict:
            return {
                'r': int(color_dict[1:3], 16),
                'g': int(color_dict[3:5], 16),
                'b': int(color_dict[5:7], 16)
            }
