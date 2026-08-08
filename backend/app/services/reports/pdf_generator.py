from reportlab.lib.pagesizes import A4 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer 
from reportlab.lib import colors 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.lib.units import inch 
from datetime import datetime 
import os 
 
def generate_beneficiary_report(beneficiaries, filename=None): 
    if filename is None: 
        filename = f"beneficiary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf" 
 
    doc = SimpleDocTemplate(filename, pagesize=A4) 
    styles = getSampleStyleSheet() 
    story = [] 
 
    # Title 
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, spaceAfter=30) 
    story.append(Paragraph("RLSD-Tracker Beneficiary Report", title_style)) 
    story.append(Spacer(1, 20)) 
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal'])) 
    story.append(Spacer(1, 20)) 
 
    # Table data 
    data = [["ID", "Name", "Gender", "Village", "Block", "District", "Income"]] 
    for b in beneficiaries: 
        data.append([ 
            b.get('beneficiary_id', ''), 
            b.get('full_name', ''), 
            b.get('gender', ''), 
            b.get('village', ''), 
            b.get('block', ''), 
            b.get('district', ''), 
            str(b.get('family_income', '')) 
        ]) 
 
    table = Table(data) 
    table.setStyle(TableStyle([ 
        ('BACKGROUND', (0,0), (-1,0), colors.grey), 
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), 
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), 
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), 
        ('FONTSIZE', (0,0), (-1,0), 12), 
        ('BOTTOMPADDING', (0,0), (-1,0), 12), 
        ('BACKGROUND', (0,1), (-1,-1), colors.beige), 
        ('GRID', (0,0), (-1,-1), 1, colors.black) 
    ])) 
 
    story.append(table) 
    story.append(Spacer(1, 20)) 
    story.append(Paragraph(f"Total Beneficiaries: {len(beneficiaries)}", styles['Normal'])) 
 
    doc.build(story) 
    return filename 
