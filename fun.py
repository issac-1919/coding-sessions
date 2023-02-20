def translate_name(name):
    name = name.upper().replace(" ","")
    print(name)
    d = create_alpha_dict()
    s = ""
    for ind in range(len(name)):
        s = s + str(d[name[ind]]) + "-"
    return s

def create_alpha_dict():
    alpha_dict = {}
    for i in range(65, 91):
        alpha_dict[chr(i)] = i - 64
    print (alpha_dict)
    return (alpha_dict)

def gen_ints(x):
    for i in range(x):
        (yield i)
