# Practical 128: Name all 118 elements Quiz Game
elements = [
    'hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon',
    'sodium', 'magnesium', 'aluminium', 'silicon', 'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium',
    'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc',
    'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium',
    'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin',
    'antimony', 'tellurium', 'iodine', 'xenon', 'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium',
    'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium',
    'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury',
    'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium',
    'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium',
    'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium',
    'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 'livermorium', 'tennessine', 'oganesson'
]

#ask the user for input
def userinput():
    remaining = elements.copy()
    guessed = []

    while remaining:
        element = input("Enter an element: ").strip().lower()
        if not element:
            print("Please type something!")
            continue
        if element == "quit":
            print("You gave up early 😅")
            break
        if element in remaining:
            print("✅ Correct One!")
            remaining.remove(element)
            guessed.append(element)
            print(f"Elements left: {len(remaining)}")
        elif element in guessed:
            print("⚠️ Already Guessed!")
        else:
            print("❌ Incorrect!")

    if not remaining:
        print("🎉 Congratulations! You guessed all element names.")

userinput()