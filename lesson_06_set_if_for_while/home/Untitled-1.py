prompt = "Введіть начинку для піци: "

while True:
    topping = input(prompt).strip()
    
    # Перевіряємо, чи користувач не хоче вийти
    if topping.lower() == 'quit':
        print("\nДякуємо! Ваша піца готується.")
        break
    
    # Якщо введено порожній рядок, просто пропускаємо
    if not topping:
        continue
        
    print(f"-> Ми додамо {topping} до вашої піци!\n")