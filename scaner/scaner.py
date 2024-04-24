import cv2
import easyocr

def text_recognition(img):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(img, detail=False)
    for (coord, text, prob) in result:
        (topleft, topright, bottomright, bottomleft) = coord
        tx, ty = (int(topleft[0]), int(topleft[1]))
        bx, by = (int(bottomright[0]), int(bottomright[1]))
        cv2.rectangle(img, (tx, ty), (bx, by), (0, 0, 255), 2)

    cv2.imshow(img)
    # digit_result = []
    # for i in result:
    #         digit_result.append(i)
  #  return digit_result

def main():
    # Путь к файлу, который будет передан на распознавание
    file_path = 'photo2.jpg'
    img = cv2.imread(file_path)
   # cv2.imshow(img)# Путь к файлу, который будет передан на распознавание
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(img, detail=1,paragraph=False)
    digit_result = []
    for i in result:
       print(i[1])
       if i[1].isdigit():
           digit_result.append(i)
    for (coord, text, prob) in digit_result:
        (topleft, topright, bottomright, bottomleft) = coord
        tx, ty = (int(topleft[0]), int(topleft[1]))
        bx, by = (int(bottomright[0]), int(bottomright[1]))
        cv2.rectangle(img, (tx, ty), (bx, by), (0, 0, 255), 2)
    cv2.imshow('Decoded Image',img)
    cv2.waitKey(60000)

    # Распознавание текста на изображении
 #   result = text_recognition(file_path)
    # Вывод результатов

if __name__ == "__main__":
    main()