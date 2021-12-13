from fpdf import FPDF
from datetime import datetime

title = 'Intrusion Prevention System'
now = datetime.now()


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(250, 250, 250)
        self.set_line_width(1)
        self.cell(w, 9, title, 1, 1, 'C', 1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, 'List of today\'s events %s' % (now.strftime("%d/%m/%Y")), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, list_of_events):
        self.set_font('Times', '', 12)
        for loe in list_of_events:
            self.cell(200, 10, txt=loe, ln=1, align='C')
        self.ln()
        self.set_font('', 'I')
        self.cell(0, 5, '(end of report)')

    def print_chapter(self, list_of_events):
        self.add_page()
        self.chapter_title()
        self.chapter_body(list_of_events)


def save_report(list_of_events):
    pdf = PDF()
    pdf.set_title(title)
    pdf.set_author('Intrusion Prevention System')
    pdf.print_chapter(list_of_events)
    pdf.output('Report of today\'s events %s.pdf' % (now.strftime("%d-%m-%Y")), 'F')

