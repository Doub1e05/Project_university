import cv2
import easyocr

def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=False)
    digit_result = []
    for i in result:
        if i.isdigit():
            digit_result.append(i)
    return digit_result

def main():
    # Путь к файлу, который будет передан на распознавание
    file_path = 'captured_image.jpg'  # Путь к файлу, который будет передан на распознавание
    print("Recognizing text from the captured image...")
    # Распознавание текста на изображении
    result = text_recognition(file_path)
    # Вывод результатов
    print("Text recognition result:", result)

if __name__ == "__main__":
    main()