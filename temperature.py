def convert_to_celcius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degree.
    
    >>>convert_to_celcius(32)
    0.0
    >>>convert_to_celcius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9
