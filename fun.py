def translate_name(name):
    name = name.upper().replace(" ","")
    d = create_alpha_dict()
    return "ok"

def create_alpha_dict():
    alpha_dict = {}
    for i in range(65, 91):
        alpha_dict[chr(i)] = i - 64
    print (alpha_dict)
    return (alpha_dict)
    
translate_name("ab")