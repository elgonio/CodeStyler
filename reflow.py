import pprint
import yaml

def process_curly_brackets(file_as_list, settings):
    og_code = file_as_list
    new_code = og_code
    if settings["curly_bracket_style"] == "NEWLINE":
        print "style is newline"
        count = 0
        for line in og_code:
            if len(line.strip()) > 1 and line.strip()[-1] == '{' :
                new_code.insert(count+1, "{")
                pos = line.find('{')
                new_line = line[:pos-1] + line[(pos+1):]
                new_code[count] = new_line

            count = count + 1
    return new_code

def process_indentation(file_as_list, settings):
    og_code = file_as_list
    new_code = og_code
    indent_size = settings["indent_size"]
    count = 0
    indent_level = 0
    
    for line in og_code:
        for char in line:
            if char == '{':
                new_line = (" " * indent_size * indent_level) + line.strip() + "\n"
                new_code[count] = new_line
                indent_level = indent_level + 1
            elif char == '}':
                indent_level = indent_level - 1
                new_line = (" " * indent_size * indent_level) + line.strip() + "\n"
                new_code[count] = new_line
            else:
                new_line = (" " * indent_size * indent_level) + line.strip() + "\n"
                new_code[count] = new_line

        count = count + 1

    return new_code





with open("settings.yaml") as style:
    style_y = yaml.load(style)
    print style_y
    print(style_y['indent_size'])


filename = raw_input("input filename \n")
with open(filename) as code:
    og_code = code.readlines()

new_code = process_curly_brackets(og_code,style_y)
new_code = process_indentation(new_code,style_y)

if style_y["replace_file"] != True:
    print "THISWORKS"
    parts = filename.split(".")
    filename = parts[0] + "_REFLOWED" + "." + parts[1]

with open (filename, 'w+') as output:
    for item in new_code:
        output.write("%s" % item)

pprint.pprint(new_code)
