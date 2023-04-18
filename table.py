# Define the data to be displayed in the table
table_data = [
    ['Name', 'Age', 'Gender'],
    ['John', '25', 'Male'],
    ['Jane', '30', 'Female'],
    ['Bob', '45', 'Male']
]

# Create an empty string to hold the HTML code
html_code = ""

# Open the table tag
html_code += "<h1> Train Stop Timetable </h1>"
html_code += "<table style='  border-collapse: collapse; width: 100%; max-width: 800px; margin: 0 auto;'>"

# Loop through each row of data and create a table row
for row in table_data:
    html_code += "<tr>"
    for item in row:
        # Create a table cell for each item in the row
        html_code += "<td>{}</td>".format(item)
    html_code += "</tr>"

# Close the table tag
html_code += "</table>"

# Print the final HTML code
print(html_code)

with open("table.html", "w") as file:
    file.write(html_code)
