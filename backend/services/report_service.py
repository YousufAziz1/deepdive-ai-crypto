from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import io
from datetime import datetime
from typing import Dict
import os

from models.schemas import AnalysisResponse
from config import settings

class ReportService:
    """Generate beautiful PDF reports"""
    
    def __init__(self):
        self.reports_dir = settings.REPORTS_DIR
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def generate_report(self, analysis: AnalysisResponse) -> str:
        """Generate comprehensive PDF report"""
        
        # Create filename
        project_name = analysis.project_data.project_name.replace(" ", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_{timestamp}.pdf"
        filepath = os.path.join(self.reports_dir, filename)
        
        # Create PDF
        doc = SimpleDocTemplate(filepath, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=12,
            spaceBefore=12
        )
        
        # Title
        story.append(Paragraph(f"DeepDive AI Research Report", title_style))
        story.append(Paragraph(f"{analysis.project_data.project_name}", styles['Heading2']))
        story.append(Spacer(1, 0.2*inch))
        
        # Executive Summary
        story.append(Paragraph("Executive Summary", heading_style))
        story.append(Paragraph(analysis.executive_summary, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Key Metrics Table
        story.append(Paragraph("Key Metrics", heading_style))
        metrics_data = [
            ['Metric', 'Value'],
            ['Price', f"${analysis.project_data.token_metrics.price or 0:.4f}"],
            ['Market Cap', f"${analysis.project_data.token_metrics.market_cap or 0:,.0f}"],
            ['24h Volume', f"${analysis.project_data.token_metrics.volume_24h or 0:,.0f}"],
            ['FDV', f"${analysis.project_data.token_metrics.fully_diluted_valuation or 0:,.0f}"],
        ]
        
        metrics_table = Table(metrics_data, colWidths=[3*inch, 3*inch])
        metrics_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(metrics_table)
        story.append(Spacer(1, 0.3*inch))
        
        # Scores Section
        story.append(Paragraph("Analysis Scores", heading_style))
        scores_data = [
            ['Category', 'Score'],
            ['Team Credibility', f"{analysis.scores.team_credibility}/10"],
            ['Product-Market Fit', f"{analysis.scores.product_market_fit}/10"],
            ['Tokenomics Health', f"{analysis.scores.tokenomics_health}/10"],
            ['Community Strength', f"{analysis.scores.community_strength}/10"],
            ['Technical Development', f"{analysis.scores.technical_development}/10"],
            ['TOTAL', f"{analysis.scores.total}/50"],
        ]
        
        scores_table = Table(scores_data, colWidths=[3*inch, 3*inch])
        scores_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2ecc71')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#f39c12')),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(scores_table)
        story.append(Spacer(1, 0.3*inch))
        
        # Risk Assessment
        story.append(Paragraph("Risk Assessment", heading_style))
        risk_color = {
            'green': colors.green,
            'yellow': colors.yellow,
            'red': colors.red
        }.get(analysis.risk_flags.level, colors.grey)
        
        risk_text = f"<font color='{risk_color.hexval()}'>●</font> Risk Level: {analysis.risk_flags.level.upper()}"
        story.append(Paragraph(risk_text, styles['Normal']))
        
        if analysis.risk_flags.flags:
            story.append(Paragraph("Risk Flags:", styles['Normal']))
            for flag in analysis.risk_flags.flags:
                story.append(Paragraph(f"• {flag}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Investment Thesis
        story.append(PageBreak())
        story.append(Paragraph("Investment Thesis", heading_style))
        
        story.append(Paragraph("<b>Bull Case:</b>", styles['Normal']))
        for point in analysis.investment_thesis.bull_case:
            story.append(Paragraph(f"✓ {point}", styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        story.append(Paragraph("<b>Bear Case:</b>", styles['Normal']))
        for point in analysis.investment_thesis.bear_case:
            story.append(Paragraph(f"✗ {point}", styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        story.append(Paragraph(f"<b>Recommendation:</b> {analysis.investment_thesis.recommendation}", 
                             styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Footer
        story.append(Spacer(1, 0.5*inch))
        footer_text = f"Generated by DeepDive AI | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        story.append(Paragraph(footer_text, styles['Normal']))
        
        # Build PDF
        doc.build(story)
        
        return filename
    
    def generate_comparison_report(self, comparison_data: Dict) -> str:
        """Generate comparison report for multiple projects"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"comparison_{timestamp}.pdf"
        filepath = os.path.join(self.reports_dir, filename)
        
        doc = SimpleDocTemplate(filepath, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        story.append(Paragraph("Project Comparison Report", styles['Title']))
        story.append(Spacer(1, 0.3*inch))
        
        # Comparison table
        projects = comparison_data.get('projects', [])
        if projects:
            comparison_data_table = [
                ['Project', 'Score', 'Risk', 'Recommendation']
            ]
            
            for analysis in projects:
                comparison_data_table.append([
                    analysis.project_data.project_name,
                    f"{analysis.scores.total}/50",
                    analysis.risk_flags.level.upper(),
                    analysis.investment_thesis.recommendation
                ])
            
            table = Table(comparison_data_table, colWidths=[2*inch, 1.5*inch, 1.5*inch, 2*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
        
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph("Comparative Analysis", styles['Heading2']))
        story.append(Paragraph(comparison_data.get('comparative_summary', ''), styles['Normal']))
        
        doc.build(story)
        return filename
