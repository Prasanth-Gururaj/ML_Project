def get_signed_number(text):
    sign = ''
    number = ''
    decimal_point = False
    digit = False

    for char in text:
        if char.isdigit():
            if not digit:
                digit = True
                number += char
            else:
                number += char
        elif char in '+-' and not digit:
            sign = char
        elif char == '.' and digit and not decimal_point:
            number += char  
            decimal_point = True

    if digit:
        return sign + number
    return None  

input_text = "abc-a2lj42k-6b.ajjlsf23jh"
result = get_signed_number(input_text)

print(result) 
