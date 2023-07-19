import re

string = "hihasdlkf1:: &#@($ ) hi4$jd "
newString = re.sub(r'[\W_]', '', string)
print(newString)