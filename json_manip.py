import json
example_input = '''{
            "page_number": 1,
            "index_on_page": 1,
            "n_rows": 5,
            "n_columns": 2,
            "title": "Weekly Winners (ASW)",
            "subtitle": "Bond",
            "type": "Generic",
            "values_type": "Numerical",
            "geo_bounds": {
                "left": 61.8,
                "top": 13.2,
                "right": 92.4,
                "bottom": 22.2
            },
            "row_captions": {
                "(01, 00)": "CDEP 1.5 6/24",
                "(02, 00)": "NRW 1.375 1/20",
                "(03, 00)": "Q 0.2 4/25",
                "(04, 00)": "Q 1.125 10/25",
                "(05, 00)": "Q 2.25 7/23"
            },
            "column_captions": {
                "(00, 01)": "current ASW",
                "(00, 02)": "1w change"
            },
            "values": {
                "(01, 01)": "86.9",
                "(01, 02)": "-7.5",
                "(02, 01)": "117.4",
                "(02, 02)": "-5.7",
                "(03, 01)": "12.3",
                "(03, 02)": "-4.8",
                "(04, 01)": "13.5",
                "(04, 02)": "-4.6",
                "(05, 01)": "8.1",
                "(05, 02)": "-4.5"
            },
            "generated_by": "reap",
            "validated": false
        }'''
example_shift = 4


#function to shift column key values in an inputted json by a constant shift - for files which have split tables
def column_shift(input, shift):
    loaded = json.loads(input)
    new_keys = []
    old_keys = []
    for v in loaded["values"]:
        column_s = v[5:-1]
        new_int = int(column_s) + shift
        new_str = ""
        if (new_int<10):
            new_str = '0' + str(new_int)
        else:
            new_str = str(new_int)
        new_key = v[:5] + new_str + v[-1:]
        new_keys.append(new_key)
        old_keys.append(v)
    for i in range(len(new_keys)):
        loaded["values"][new_keys[i]] = loaded["values"].pop(old_keys[i])
    print(json.dumps(loaded, sort_keys=False, indent=4))

#function to shift row key values in an inputted json by a constant shift - for files which have split tables
def row_shift(input, shift):
    loaded = json.loads(input)
    new_keys = []
    old_keys = []
    for v in loaded["values"]:
        row_s = v[1:-5]
        new_int = int(row_s) + shift
        new_str = ""
        if (new_int<10):
            new_str = '0' + str(new_int)
        else:
            new_str = str(new_int)
        new_key = v[:1] + new_str + v[-5:]
        new_keys.append(new_key)
        old_keys.append(v)
    values = []
    for i in range(len(new_keys)):
        values.append(loaded["values"].pop(old_keys[i]))
    for i in range(len(new_keys)):
        loaded["values"][new_keys[i]] = values[i]
    print(json.dumps(loaded, sort_keys=False, indent=4))

#function to shift column caption key values in an inputted json by a constant shift - for files which have split tables
def column_caption_shift(input, shift):
    loaded = json.loads(input)
    new_keys = []
    old_keys = []
    for v in loaded["column_captions"]:
        column_s = v[5:-1]
        new_int = int(column_s) + shift
        new_str = ""
        if (new_int<10):
            new_str = '0' + str(new_int)
        else:
            new_str = str(new_int)
        new_key = v[:5] + new_str + v[-1:]
        new_keys.append(new_key)
        old_keys.append(v)
    print(new_keys)
    print(old_keys)
    values = []
    for i in range(len(new_keys)):
        values.append(loaded["column_captions"].pop(old_keys[i]))
    for i in range(len(new_keys)):
        loaded["column_captions"][new_keys[i]] = values[i]
    print(json.dumps(loaded, sort_keys=False, indent=4))

#function to shift row caption key values in an inputted json by a constant shift - for files which have split tables
def row_caption_shift(input, shift):
    loaded = json.loads(input)
    new_keys = []
    old_keys = []
    for v in loaded["row_captions"]:
        row_s = v[1:-5]
        new_int = int(row_s) + shift
        new_str = ""
        if (new_int<10):
            new_str = '0' + str(new_int)
        else:
            new_str = str(new_int)
        new_key = v[:1] + new_str + v[-5:]
        new_keys.append(new_key)
        old_keys.append(v)
    values = []
    for i in range(len(new_keys)):
        values.append(loaded["row_captions"].pop(old_keys[i]))
    for i in range(len(new_keys)):
        loaded["row_captions"][new_keys[i]] = values[i]
    print(json.dumps(loaded, sort_keys=False, indent=4))

#column_shift(example_input, example_shift)
#row_shift(example_input, example_shift)
#column_caption_shift(example_input, example_shift)
#row_caption_shift(example_input, example_shift)