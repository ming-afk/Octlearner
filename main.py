# import xlsxwriter


list = {'michael', 'Jason', 'Peter'}

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, list)

workbook.close()
