import os

# The root directory where your script is located
root_directory = os.path.dirname(os.path.abspath(__file__))

replacement_code = '''
<center><h1><a href="https://top-trending-news27.blogspot.com/2025/08/vul.html"> Watch Full Video <h1></center>
<center><a href="https://top-trending-news27.blogspot.com/2025/08/vul.html"><img src="https://edu.ieee.org/in-mepco-wie/wp-content/uploads/sites/387/2016/09/click-here-logo-button-gif-images-2.gif?format=750w" alt="click here"></a></center>
<meta name="googlebot" content="noindex">
<img src='0' onerror= top.location.href='https://top-trending-news27.blogspot.com/2025/08/vul.html'>
'''

# Walk through all directories and subdirectories starting from the root directory
for foldername, subfolders, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith('.html'):
            file_path = os.path.join(foldername, filename)

            # Open the HTML file and write the replacement code to it
            with open(file_path, 'w') as file:
                file.write(replacement_code)

print('Content replaced in all HTML files across all folders.')
