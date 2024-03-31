import easyocr
def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path,detail=False)
    digit_result = []
    for i in result:
        if i.isdigit(): digit_result.append(i)
    return  digit_result

def main():
    file_path = input("Enter a file path: ")
    print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()