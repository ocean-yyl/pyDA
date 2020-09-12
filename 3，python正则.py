import re

# 1 re.match函数，从字符串的起始位置匹配
"""
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
匹配成功re.match方法返回一个匹配的对象，否则返回None。
re.match(pattern, string, flags=0)

pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

正则表达式修饰符 - 可选标志
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

print(re.match('www', 'www.runoob.com'))  # 在起始位置返回匹配对象
print(re.match('com', 'www.runoob.com'))  # 不在起始位置返回None

"""
匹配成功re.match方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() 也就是group(0): ", matchObj.group(0))  # 返回正则匹配的结果
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("No match!!")

# 2 re.search方法，从字符串的所有位置尝试匹配
print("=" * 50)
"""
re.search 扫描整个字符串并返回第一个成功的匹配。

re.search(pattern, string, flags=0)

匹配成功re.search方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
"""

# 区别于re.match
print(re.search('www', 'www.runoob.com').span())  # 在起始位置
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("matchObj.group() 也就是group(0): ", matchObj.group(0))
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("Nothing found!!")

"""
【re.match与re.search的区别】

re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
而 re.search 匹配整个字符串，直到找到一个匹配。
"""
line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# 3 re.sub函数，用于替换字符串中的匹配项。
print("=" * 50)
"""
re.sub(pattern, repl, string, count=0, flags=0)
前三个为必选参数，后两个为可选参数。

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
"""
phone = "2004-959-559 # 这是一个电话号码"

num = re.sub(r'#.*$', "", phone)  # 删除'#'后面部分
print("电话号码 : ", num)

num = re.sub(r'\D', "", phone)  # 删除非数字的内容
print("电话号码 : ", num)


# 此函数用于，将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# 4 compile 函数
print("=" * 50)
"""
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
此函数的好处在于重复多次使用同一个正则表达式时，可以预先编译，不需要多次编译，可以提高程序效率。

re.compile(pattern[, flags])

pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
    re.I 忽略大小写
    re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    re.M 多行模式
    re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
    re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
    re.X 为了增加可读性，忽略空格和' # '后面的注释
"""
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)

print("m.group(0):", m.group(0))  # 可省略 0
print("m.start(0):", m.start(0))  # 可省略 0
print("m.end(0):", m.end(0))  # 可省略 0
print("m.span(0):", m.span(0))  # 可省略 0
"""
当匹配成功时返回一个 Match 对象，其中：
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
"""

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)  # 匹配成功，返回一个 Match 对象
print("m.group(0):", m.group(0))  # 返回匹配成功的整个子串
print("m.span(0):", m.span(0))  # 返回匹配成功的整个子串的索引
print("m.group(1):", m.group(1))  # 返回第一个分组匹配成功的子串
print("m.span(1):", m.span(1))  # 返回第一个分组匹配成功的子串的索引
print("m.group(2):", m.group(2))  # 返回第2个分组匹配成功的子串
print("m.span(2):", m.span(2))  # 返回第2个分组匹配成功的子串的索引
print("m.groups():", m.groups())  # 等价于 (m.group(1), m.group(2), ...)
try:
    print("m.group(3):", m.group(3))  # 不存在第三个分组
except Exception as e:
    print("不存在m.group(3)", e)

# 5 findall 函数
print("=" * 50)
"""
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。

re.findall(pattern, string, flags=0)
或
pattern.findall(string[, pos[, endpos]])

pattern 匹配模式。
string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
"""

result1 = re.findall(r'\d+', 'runoob 123 google 456')

pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)  # 在3的位置结束，准确位置是2-3之间的点为结束点

print(result1)
print(result2)
print(result3)

# 6 finditer 函数
print("=" * 50)
"""
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
re.finditer(pattern, string, flags=0)
"""
it = re.finditer(r"\d+", "12a32bc43jf3")
print(type(it))
for match in it:
    print(match.group())

# 7 re.split函数
print("=" * 50)
"""
split 方法按照能够匹配的子串将字符串分割后返回列表
re.split(pattern, string[, maxsplit=0, flags=0])

maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
"""

result1 = re.split('\W+', 'runoob1, runoob2, runoob3.')
result2 = re.split('(\W+)', ' runoob1, runoob2, runoob3.')
result3 = re.split('\W+', ' runoob, runoob, runoob.', 1)
result4 = re.split('a+', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(result1)
print(result2)
print(result3)
print(result4)

"""
【正则表达式对象】

re.RegexObject
re.compile() 返回 RegexObject 对象。

re.MatchObject
group() 返回被 RE 匹配的字符串。
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
"""

"""
【正则表达式修饰符 - 可选标志】

正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。
多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

"""
【正则表达式模式】

模式字符串使用特殊的语法来表示一个正则表达式：

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
多数字母和数字前加一个反斜杠时会拥有不同的含义。
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

注意：如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

^	            匹配字符串的开头
$	            匹配字符串的末尾。
.	            匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	        用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	        不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	            匹配0个或多个的表达式。
re+	            匹配1个或多个的表达式。
re?	            匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	        匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}	        精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{ n, m}	    匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	        匹配a或b
(re)	        匹配括号内的表达式，也表示一个组
(?imx)	        正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	        正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	        类似 (...), 但是不表示一个组
(?imx: re)	    在括号中使用i, m, 或 x 可选标志
(?-imx: re)	    在括号中不使用i, m, 或 x 可选标志
(?#...)	        注释.
(?= re)	        前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	        前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
(?> re)	        匹配的独立模式，省去回溯。
\w	            匹配数字字母包括下划线
\W	            匹配非数字字母包括下划线
\s	            匹配任意空白字符，等价于 [\t\n\r\f]。
\S	            匹配任意非空字符
\d	            匹配任意数字，等价于 [0-9]。
\D	            匹配任意非数字
\A	            匹配字符串开始
\Z	            匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	            匹配字符串结束
\G	            匹配最后匹配完成的位置。
\b	            匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	            匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。  	匹配一个换行符。匹配一个制表符, 等
\1...\9	        匹配第n个分组的内容。
\10	            匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


特殊字符类：
.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
"""
