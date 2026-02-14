import tkinter as tk
from random import randint

# ----------------- تنظیمات اولیه -----------------
answer = None
talash = 0
max_number = 0
list1 = []

# ----------------- توابع -----------------


def setting_level(level):
    global talash, max_number, answer, list1
    list1 = []

    if level == 1:
        max_number, talash = 10, 3
    elif level == 2:
        max_number, talash = 50, 5
    elif level == 3:
        max_number, talash = 100, 6

    answer = randint(1, max_number)
    lbl_info.config(text=f"عدد بین 1 تا {max_number}")
    lbl_talash.config(text=f"تلاش باقی‌مانده: {talash}")
    lbl_result.config(text="بازی شروع شد ✅")


def check():
    global talash

    try:
        javab = int(entry.get())
    except ValueError:
        lbl_result.config(text="❌ عدد وارد کن")
        return

    list1.append(javab)
    talash -= 1

    if javab == answer:
        lbl_result.config(text="🎉 WOW! درست گفتی")
    elif javab > answer:
        lbl_result.config(text="⬇️ عددت بزرگ‌تره")
    else:
        lbl_result.config(text="⬆️ عددت کوچک‌تره")

    lbl_talash.config(text=f"تلاش باقی‌مانده: {talash}")
    lbl_list.config(text=f"حدس‌ها: {list1}")

    if talash == 0 and javab != answer:
        lbl_result.config(text=f"❌ باختی | جواب: {answer}")

    entry.delete(0, tk.END)


# ----------------- رابط گرافیکی -----------------
root = tk.Tk()
root.title("🎯 بازی حدس عدد")
root.geometry("400x450")

tk.Label(root, text="انتخاب سطح", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="آسان", width=15,
          command=lambda: setting_level(1)).pack(pady=5)
tk.Button(root, text="متوسط", width=15,
          command=lambda: setting_level(2)).pack(pady=5)
tk.Button(root, text="سخت", width=15,
          command=lambda: setting_level(3)).pack(pady=5)

lbl_info = tk.Label(root, text="", font=("Arial", 12))
lbl_info.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="بررسی", command=check).pack(pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 12))
lbl_result.pack(pady=10)

lbl_talash = tk.Label(root, text="")
lbl_talash.pack()

lbl_list = tk.Label(root, text="")
lbl_list.pack(pady=10)

root.mainloop()
