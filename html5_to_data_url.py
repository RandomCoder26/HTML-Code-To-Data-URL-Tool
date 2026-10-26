import base64

def create_data_uri():
    html5_code = """
    <!--add html5 code here-->
    <h1>filler text</h1>
    """
    html5_code_b = html5_code.encode("utf-8")
    html5_code_b64 = base64.b64encode(html5_code_b)
    b64_string = html5_code_b64.decode("utf-8")
    print("HTML5 Code To Data URI")
    print(f"Data URI: data://text/html;base64,{b64_string}")

create_data_uri()