
# Find out wich character encoding the system with:
print("cash".encode())  # b'cash'
print(list("cash".encode()))    # [99, 97, 115, 104]
print(bytes([99, 97, 115, 104]).decode())   # cash
print(bytes([99, 97, 102, 195, 169]).decode("utf-8"))   # cafe
# print(bytes([99, 97, 102, 195, 169]).decode("ascii"))   # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)

# when opening a file in Py we must tell which ch encoding is the file writen with:
# with open("basics/18_file_handling/people-100.csv", encoding="iso-88-59-2") as file: # LookupError: unknown encoding: iso-88-59-2
with open("basics/18_file_handling/people-100.csv", encoding="utf-8") as file:  # works too with ascii
    file.read()

# library to try to guess the encoding:
# chardet library will shows us wich ch encoding our python version supports:
from encodings.aliases import aliases
print(set(aliases.values())) # {'iso8859_13', 'cp857', 'euc_kr', 'iso2022_jp_ext', 'cp437', 'big5', 'utf_32', 'cp863', 'shift_jisx0213', 'utf_8', 'iso8859_14', 'cp1140', 'mac_cyrillic', 'cp1258', 'cp949', 'iso8859_15', 'iso8859_4', 'iso8859_7', 'rot_13', 'uu_codec', 'cp864', 'mbcs', 'cp869', 'kz1048', 'iso2022_jp_3', 'cp775', 'cp860', 'iso2022_jp_1', 'utf_7', 'euc_jp', 'cp500', 'cp858', 'utf_32_le', 'cp850', 'iso8859_10', 'iso8859_3', 'cp424', 'euc_jisx0213', 'iso8859_6', 'koi8_r', 'utf_16_le', 'iso8859_2', 'cp1256', 'ptcp154', 'cp950', 'shift_jis', 'hp_roman8', 'cp1257', 'cp866', 'ascii', 'big5hkscs', 'gbk', 'base64_codec', 'utf_16', 'mac_roman', 'cp1251', 'iso2022_jp_2004', 'hz', 'hex_codec', 'utf_16_be', 'cp862', 'gb2312', 'bz2_codec', 'cp855', 'quopri_codec', 'cp1253', 'mac_iceland', 'euc_jis_2004', 'iso8859_9', 'iso8859_16', 'cp852', 'iso8859_8', 'cp037', 'cp273', 'iso2022_jp', 'mac_greek', 'mac_latin2', 'cp1252', 'iso2022_kr', 'cp1250', 'iso2022_jp_2', 'cp865', 'gb18030', 'johab', 'cp1125', 'mac_turkish', 'cp1255', 'cp932', 'iso8859_11', 'latin_1', 'zlib_codec', 'utf_32_be', 'iso8859_5', 'cp1026', 'cp1254', 'shift_jis_2004', 'tis_620', 'cp861'}