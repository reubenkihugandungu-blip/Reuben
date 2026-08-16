meals_log = ['Rice', 'Ugali', 'Chapati', 'Pilau', '6', 'Githeri']
for m in meals_log:
    try:
        meals = str(m)
    except TypeError:
        print(f"Invalid Data")
