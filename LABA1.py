class Toothbrush():
    """Зубна щітка"""
    count = 0

    @staticmethod
    def getCount():
        return Toothbrush.count

    def __init__(self, color, weight_grams, cleaning_modes):
        """Ініціалізація атрибутів"""
        Toothbrush.count += 1
        self.color = color
        self.weight_grams = weight_grams
        self.cleaning_modes = cleaning_modes


    def __str__(self):
        """Створення шаблону """
        return f"Toothbrush color: {self.color} \n" \
               f"Toothbrush weight: {self.weight_grams} \n" \
               f"Toothbrush cleaning modes: {self.cleaning_modes} \n" \


    def __del__(self):
        """Деконструктор"""
        Toothbrush.count -= 1

def main():
    """Присвоєння значеннь та виведення"""
    first_toothbrush = Toothbrush("Black", 830, "Total destruction")
    second_toothbrush = Toothbrush("White", 750, "Reverse-rotational & Pulsating")
    third_toothbrush = Toothbrush("Orange", 430, "manual cleaning")
    print(first_toothbrush.__str__())
    print(second_toothbrush.__str__())
    print(third_toothbrush.__str__())
    print(f"number of objects in the class: {Toothbrush.getCount()} ")

"""Точка входу"""
if __name__ == "__main__":
    main()