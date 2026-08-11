# 
import io
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
print("File written. Contents:")
print(file_content.getvalue())