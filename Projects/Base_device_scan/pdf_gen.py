# -*- coding: utf-8 -*-

import collections
from datetime import datetime as dt
from os import remove as rm
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

class gen_pdf:

  def __init__(self, class_check):
    self.class_check = class_check
    self.canv = canvas.Canvas('plik.pdf', pagesize=A4)
    drive = ''
    self.width, self.height = A4
    #print(width, height)
    #'Bios': 'bios_info',
    file_collection = {'01Bateria': drive + 'battery_info.txt', '02Model': drive + 'cpu_model_info.txt',
                 '03Dysk': drive + 'disc_info.txt', '04Napedy': drive + 'drive_info.txt', '05Grafika': drive + 'graphic_info.txt',
                 '06Procesor [ToDo]': drive + 'proc_info.txt', '07Ram': drive + 'ram_info.txt', '08Ekran': drive + 'screen_info.txt',
                 '09Wifi': drive + 'wifi_check.txt', '10': drive + 'comment_file.txt'}
    self.file_collection = collections.OrderedDict(sorted(file_collection.items()))

    self.time = dt.now()
    self.time = self.time.strftime("%H:%M %d.%m.%Y")

    #Add font
    pdfmetrics.registerFont(TTFont('Monospace', 'FreeMono.ttf'))
    self.import_png()
    self.text_from_file()
    self.save_pdf()


  def import_png(self):
    #Add coda png
    self.height_text = self.height
    var = self.canv.drawImage('draw-img.gif', self.width, self.height)
    self.canv.drawImage('draw-img.gif', (self.width-var[0])/2, 20)
    self.height_text -= 30

  def text_from_file(self):
    #Add specyfication from text
    for regio in self.file_collection:
      self.canv.setFont("Monospace",size=12)
      self.canv.drawString(40,(self.height_text), regio[2::])
      self.height_text -= 18
      #print(self.file_collection.get(regio))
      try:
        with open(self.file_collection.get(regio), 'r') as specification:
          lines_specification = specification.readlines()
          for line_specification in lines_specification:
            self.canv.drawString(50, (self.height_text), line_specification[:-1])
            self.height_text -= 18
      except Exception as open_file_problem:
        self.error_log("Open file to pdf", open_file_problem)

    #
    stylesheet = getSampleStyleSheet()
    styleN = stylesheet['Normal']
    styleN.fontSize = 14
    styleN.fontName = 'Monospace'
    p = Paragraph(u'<para align="center">CPU Reader <u>v1.03</u></para>', styleN)
    p.wrap(self.width, self.height)
    p.drawOn(self.canv, 0, 90)

  def save_pdf(self):
    #Save to File
    print(self.class_check)
    self.canv.showPage()
    self.canv.save()

  def error_log(self, function, error):
    print(str(error) + '\nCheck error log!')
    log = open('Error_log.txt', 'a')
    log.write('{}# in function {}\n{}\nFile named: {}\n'.format(self.time, function, str(error), str(__file__)))
    return 0

if __name__=="__main__":
  gen_pdf('B')
