def make_order(table_number, *args, **kwargs):
    print(f"ЗАКАЗ ДЛЯ СТОЛИКА №{table_number}")
    if args:
        for i,dish in enumerate(args,1):
            print(f"{i}) {dish}")
    if kwargs:
        print("Пожелания:")
        for key,value in kwargs.items():
            print(f"{key}: {value}")
make_order(5, "Пицца", "Кола", time="19:30", spicy=False)