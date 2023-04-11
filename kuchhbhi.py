from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

# Create a new PDF document
pdf = SimpleDocTemplcloate('example.pdf', pagesize=A4)

# Define a list of data for the table
data = [['Name', 'Age', 'Gender'],
        ['John', '25', 'Male'],
        ['Jane', '30', 'Female'],
        ['Bob', '45', 'Male']]

# Create a table with the data
table = Table(data)

# Define table style
style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),                                        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),                                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),                                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),                                        ('FONTSIZE', (0,0), (-1,0), 14),                                        ('BOTTOMPADDING', (0,0), (-1,0), 12),                                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),                                        ('GRID', (0,0), (-1,-1), 1, colors.black)])

# Apply table style
table.setStyle(style)

# Define image to be added to PDF document
logo = Image('logo.png', width=2*inch, height=2*inch)

# Set opacity of image to 0.5
logo.set_alpha(0.5)

# Create a list of elements to be added to PDF document
elements = [logo, table]

# Add elements to PDF document and save to file
pdf.build(elements)
