from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(str(entry) for entry in data))

    print(f"Log file '{filename}' has been created successfully.")

    return filename
