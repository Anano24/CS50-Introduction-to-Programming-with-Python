answer = input("File name: ")

new_answer = answer.lower().strip()

if new_answer.endswith(".gif"):
    print("image/gif")
elif new_answer.endswith(".jpeg") or new_answer.endswith(".jpg"):
    print("image/jpeg")
elif new_answer.endswith("png"):
    print("image/png")
elif new_answer.endswith(".pdf"):
    print("application/pdf")
elif new_answer.endswith(".txt"):
    print("text/plain")
elif new_answer.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
