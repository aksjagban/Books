# Program returns a report with grouped languages of books from "book.xml".
import re

#Reading XML file:
f = open('book.xml')
try:
	text = f.read()
finally:
	f.close()

#Creating list of translation units.
tuRegex = r'\<book.*?\<\/book\>'
values = re.findall(tuRegex, text, re.DOTALL)

#Creating dictionary of languages as a unique key and books as a value.
dic = {}
for i in values:
	creationdateRegex = re.compile(r'(?<=<language>).*?(?=<\/language>)')
	keys = creationdateRegex.search(i)
	dic.update({keys.group(): i})

#Creating report as a TXT file:
report = "\n".join(dic.keys())
print report
text_file = open("report.txt", "w")
text_file.write(report)
text_file.close()
