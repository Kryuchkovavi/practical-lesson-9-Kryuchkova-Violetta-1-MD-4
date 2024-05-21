from PIL import Image, ImageFilter
import os

def z1():
    output_folder = 'p1'
    os.makedirs(output_folder)

    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            with Image.open(filename) as img:
                pr_img = img.filter(ImageFilter.CONTOUR)
                pr_img.save(os.path.join(output_folder, 'new_' + filename))

def z2():
    itogST = 0
    shopping_list = []

    with open('данные.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            if len(data) == 3:
                product, quantity, price = data
                cost = int(quantity) * int(price)
                itogST += cost
                shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")

    print("Нужно купить:")
    for i in shopping_list:
        print(i)

    print(f"Итоговая сумма: {itogST} руб.")

z2()


