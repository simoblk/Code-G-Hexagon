# G-code Hexagon Generator

A Python script that generates G-code for machining a hexagon shape on a CNC machine. The script takes user inputs for `SW` (width parameter) and an optional `Z` line command to customize the toolpath.

## Features
- Calculates `X` and `C` coordinates dynamically based on the input `SW` value.
- Supports optional customization of the `Z` axis movement.
- Outputs G-code with tool compensation (G42/G40) and precise positioning.

## Usage
1. Run the script in a Python environment.
2. Enter the `SW` value when prompted.
3. Optionally, provide a custom `Z` line command (e.g., `G01Z-27F5000`) or press Enter to use the default.
4. The script will output the generated G-code, which can be copied to your CNC machine's controller.

## Example
```python
Dkhal SW: 22
Dakhl code dyal G01Z.... (ex: G01Z-27F5000) Ola click 3la enter bach tb9a hya: 

G112
G01Z-27F5000
G01G42X140C0
G01X40
G01X25.4C0F700
G01X12.7C11.0
G01X-12.7C11.0
G01X-25.5C0
G01X-12.7C-11.0
G01X12.7C-11.0
G01X25.4C0
G01X12.7C11.0
G1G40X140C0F5000
G01X140C0
G01Z20
G113
