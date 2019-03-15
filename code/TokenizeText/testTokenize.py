import TokenizeText.tokenizeText as tk
import sys

print(tk.tokenize("Những ngày tiếp theo, gió mùa đông bắc tràn xuống, nhưng lệch đông. Đông Bắc Bộ, Bắc Trung Bộ sẽ đón ngày quốc tế phụ nữ 8/3 trong tiết trời mưa lạnh, nhiệt độ Hà Nội 19-20; Lạng Sơn 14-16. Tây Bắc Bộ, Trung Trung Bộ trở vào đến Nam Trung Bộ trời nắng 29-32 độ C."))

print(tk.tokenize("học sinh học sinh vật học"))
print(tk.tokenize('''X là dữ liệu features, chúng ta chuẩn bị ở dạng dictionary. Mỗi âm (syllable) được tính và tạo ra một dữ liệu đặc trưng dạng json. Ví dụ: với câu “Hello World” sẽ có 2 syllables là “Hello” và “World”. Syllable là “Hello” sẽ tạo ra 1 dict là {‘bias’: 1.0, ‘lower’: ‘hello’}. Một số các feature chúng ta có thể tính là: ‘bias’, ‘lower’, ‘isupper’, ‘istitle’, ‘isdigit’. Lưu ý: feature của một từ còn được tính cho các từ phía trước phía sau. Ví dụ: ‘+1:lower’: ‘world’ là 1 feature của “Hello”. Tương ứng với mỗi syllable (ví dụ “Hello”) là một nhãn, chẳng hạn ‘B’ hay ‘I’ (bạn có thể thay là ‘0’ hoặc ‘1’)'''))
print(tk.tokenize("""nhatnor123@gmail.com.vn https://forum.machinelearningcoban.com/t/vnlp-core-1-bai-toan-tach-tu-tieng-viet-tokenization-word-segmentation/2002"""))

specials = ["==>", "->", "\.\.\.", ">>"]
digit = "\d+([\.,_]\d+)+"
email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
datetime = [
    "\d{1,2}\/\d{1,2}(\/\d+)?",
    "\d{1,2}-\d{1,2}(-\d+)?",
]
word = "\w+"
non_word = "[^\w\s]"
abbreviations = [
    "[A-ZĐ]+\.",
    "Tp\.",
    "Mr\.", "Mrs\.", "Ms\.",
    "Dr\.", "ThS\."
]

patterns = []
patterns.extend(abbreviations)
patterns.extend(specials)
patterns.extend([web, email])
patterns.extend(datetime)
patterns.extend([digit, non_word, word])

patterns = "(" + "|".join(patterns) + ")"
if sys.version_info < (3, 0):
    patterns = patterns.decode('utf-8')

print(patterns)

print(tk.tokenize("môn học xử lý ngôn ngữ tự nhiên, con ngựa đá đá con ngựa đá"))