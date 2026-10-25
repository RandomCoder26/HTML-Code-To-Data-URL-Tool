import base64

html_code = b"""
<!--add your html5 code here-->
"""
html_code_base64_encoded = base64.urlsafe_b64encode(html_code) 
html_code_base64_encoded_clean = html_code_base64_encoded.decode("utf-8") #removes b'' from the base64 encoding

print("HTML5 Code To Data URL Converter")
print(f"Data URL (copy and paste): data:text/html;base64,{html_code_base64_encoded_clean}")
