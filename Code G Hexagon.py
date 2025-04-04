def generate_gcode(sw, c, x_hamra, x_khadra, z_line=None):
    # Hna ghadi ngeneriw G-code 3la hsab lvalues li dkhalty
    gcode = f"""
G112
{z_line if z_line else "G01Z-27F5000"}  
G01G42X140C0
G01X40
G01X{x_hamra}C0F700  
G01X{x_khadra}C{c}  
G01X-{x_khadra}C{c}  
G01X-{x_hamra + 0.1}C0  
G01X-{x_khadra}C-{c}  
G01X{x_khadra}C-{c} 
G01X{x_hamra}C0  
G01X{x_khadra}C{c}  
G1G40X140C0F5000
G01X140C0
G01Z20
G113
"""
    return gcode

# Input dyal SW
sw = float(input("Dkhal SW: "))
c = sw / 2  # C = SW / 2
x_hamra = round(sw * (25.40 / 22), 2)  # X Hamra = SW * (25.40 / 22)
x_khadra = x_hamra / 2  # X Khadra = X Hamra / 2

# Input dyal Z Line (optional)
z_line = input("Dakhl code dyal G01Z.... (ex: G01Z-27F5000) Ola click 3la enter bach tb9a hya: ").strip()

# Khraj G-code
print(generate_gcode(sw, c, x_hamra, x_khadra, z_line if z_line else None))