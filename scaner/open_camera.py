import cv2
import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=False)
    digit_result = [i for i in result if i.isdigit()]
    return digit_result


def main():
    camera = cv2.VideoCapture(0)
    cv2.namedWindow("Camera Feed")

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Ошибка при считывании изображения с камеры.")
            break

        cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):  # Нажмите 'q', чтобы выйти из программы
            break
        elif key == ord('c'):  # Нажмите 'c', чтобы сделать снимок
            cv2.imwrite('captured_image.jpg', frame)
            print("Фото успешно сохранено!")
            digit_result = text_recognition('captured_image.jpg')
            print("Результат распознавания текста:", digit_result)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()