from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
from reportlab.platypus import Paragraph

def generate_pdf(file_path, data):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []

    # Define table data
    table_data = [
        ['Employee ID', 'Number of Hours', 'Unit Price', 'Cost'],
    ]

    total_cost = data[0]["total"]

    for row in data[1]:
        duration = row['duration']
        unit_price = row['unit_price']
        cost = row['cost']

        table_data.append([
          
            row['employee_id'],
            duration,
            f"${unit_price}",
            f"${cost}",
        ])

    # Create table style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.blue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create table
    invoice_table = Table(table_data, style=style)

    company_name = Paragraph(f"<para align=left leftIndent=100>Company: Affinity labs </para>")
    elements.append(company_name)

    # Add table to the elements list
    elements.append(invoice_table)

    # Add total cost to elements as a Paragraph
    total_cost_paragraph = Paragraph(f"<para align=right rightIndent=100>Total Cost: ${total_cost}</para>")
    elements.append(total_cost_paragraph)

    # Build the PDF document
    doc.build(elements)


