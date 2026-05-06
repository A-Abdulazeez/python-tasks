def fahrenheit(celsius):
    """Return Fahrenheit equivalent of a Celsius temperature."""
    return (9 / 5) * celsius + 32


print(f'{"Celsius":>10}{"Fahrenheit":>15}')
for celsius in range(101):
    print(f'{celsius:>10}{fahrenheit(celsius):>15.1f}')
