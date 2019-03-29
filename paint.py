import glob
import styles
import xlwt
import xlrd
import sys
import styles as styles
from shutil import copyfile
import optparse

parser = optparse.OptionParser(version='0.1', usage="usage: %prog [options] file")
parser.add_option("-f", "--file", help="input file name .xls")

options,arguments=parser.parse_args()
filename=options.__dict__['file']

def set_width(sheet,wb):
	row0=sheet.col(0)
	row1=sheet.col(1)
	row2=sheet.col(2)
	row3=sheet.col(3)
	row4=sheet.col(4)
	row5=sheet.col(5)
	row6=sheet.col(6)
	row7=sheet.col(7)
	row8=sheet.col(8)
	row9=sheet.col(9)
	row10=sheet.col(10)
	row11=sheet.col(11)
	row12=sheet.col(12)

	row0.width = 9 * 250
	row1.width = 16 * 250
	row2.width = 16 * 250
	row3.width = 9 * 250
	row4.width = 13 * 250
	row5.width = 9 * 250
	row6.width = 9 * 250
	row7.width = 33 * 250
	row8.width = 22 * 250
	row9.width = 60 * 250
	row10.width = 35 * 250
	row11.width = 35 * 250
	row12.width = 35 * 250

normal = xlwt.XFStyle()
normal.alignment.wrap = 1
normal.font.height = 220
normal.font.name = 'Calibri'


def format_and_paint(filename, wb):
	rb = xlrd.open_workbook(filename)
	input_sheet = rb.sheet_by_index(0)
	sheet = wb.add_sheet('Vulnerability scan results', cell_overwrite_ok=True)
	if input_sheet.nrows < 1:
		print('No information')
	else:
		for colnum in range(input_sheet.ncols):
			sheet.row(0).write(colnum, input_sheet.cell(0, colnum).value, styles.head_style)
		
		count=0
		cve_count=0
		port_count=0
		hostname_count=0
		for rownum in range(1, (input_sheet.nrows+1)):
			# print(rownum)
			try:
				level= styles.f2(input_sheet.cell(rownum, 3).value)
				
				## filling cells that might not be merged later##
				for colnum in range(0, 12):
					if colnum == 3:
						sheet.row(rownum).write(3, input_sheet.cell(rownum, 3).value, level)
					else:
						sheet.row(rownum).write(colnum, input_sheet.cell(rownum, colnum).value, normal)
					# sheet.row(rownum).write(colnum, input_sheet.cell(rownum, colnum).value, normal)

				## comparing current row and previous one ##

				pluginid=input_sheet.cell(rownum, 0).value
				prevpluginid=input_sheet.cell(rownum - 1, 0).value

				cve = input_sheet.cell(rownum, 1).value
				prevcve = input_sheet.cell(rownum - 1, 1).value

				port = input_sheet.cell(rownum, 6).value
				prevport = input_sheet.cell(rownum - 1, 6).value

				hostname = input_sheet.cell(rownum, 4).value
				prevhostname = input_sheet.cell(rownum - 1, 4).value

				if pluginid == prevpluginid:
					count+=1
					if cve==prevcve:
						cve_count+=1
					if port == prevport:
						port_count+=1
					if hostname == prevhostname:
						hostname_count+=1
					elif hostname !=prevhostname and hostname_count>0:
						sheet.write_merge((rownum - hostname_count - 1), (rownum - 1), 4, 4, input_sheet.cell((rownum - hostname_count), 4).value, normal) # hostname
						hostname_count=0
				elif pluginid != prevpluginid and count != 0 and rownum>1:
										# print(str(rownum - count - 1)+" - " + str(rownum - 1)+ " - count = " + str(count))
					sheet.write_merge((rownum - count - 1), (rownum - 1), 0, 0, input_sheet.cell((rownum - count), 0).value, normal) # plugin id
					sheet.write_merge((rownum - count - 1), (rownum - 1), 2, 2, input_sheet.cell((rownum - count), 2).value, normal) # cvss
					sheet.write_merge((rownum - count - 1), (rownum - 1), 3, 3, input_sheet.cell((rownum - count), 3).value, styles.f2(input_sheet.cell((rownum - count), 3).value)) # severity level
					sheet.write_merge((rownum - count - 1), (rownum - 1), 5, 5, input_sheet.cell((rownum - count), 5).value, normal) # protocol
					sheet.write_merge((rownum - count - 1), (rownum - 1), 7, 7, input_sheet.cell((rownum - count), 7).value, normal) # name
					sheet.write_merge((rownum - count - 1), (rownum - 1), 8, 8, input_sheet.cell((rownum - count), 8).value, normal) # synopsis
					sheet.write_merge((rownum - count - 1), (rownum - 1), 9, 9, input_sheet.cell((rownum - count), 9).value, normal) # descr
					sheet.write_merge((rownum - count - 1), (rownum - 1), 10, 10, input_sheet.cell((rownum - count), 10).value, normal) # solution
					sheet.write_merge((rownum - count - 1), (rownum - 1), 11, 11, input_sheet.cell((rownum - count), 11).value, normal) # also
					sheet.write_merge((rownum - count - 1), (rownum - 1), 12, 12, input_sheet.cell((rownum - count), 12).value, normal) # output
					count=0

					if hostname_count>0:
						sheet.write_merge((rownum - hostname_count - 1), (rownum - 1), 4, 4, input_sheet.cell((rownum - hostname_count), 4).value, normal) # hostname
						hostname_count=0
					if cve_count!=0:
						sheet.write_merge((rownum - cve_count - 1), (rownum - 1), 1, 1, input_sheet.cell((rownum - cve_count), 1).value, normal) # cve
						cve_count=0
					if port_count!=0:
						sheet.write_merge((rownum - port_count - 1), (rownum - 1), 6, 6, input_sheet.cell((rownum - port_count), 6).value, normal) # port
						port_count=0



			except IndexError:
				if count!=0:
					sheet.write_merge((rownum - count - 1), (rownum - 1), 0, 0, input_sheet.cell((rownum - count), 0).value, normal) # plugin id
					sheet.write_merge((rownum - count - 1), (rownum - 1), 2, 2, input_sheet.cell((rownum - count), 2).value, normal) # cvss
					sheet.write_merge((rownum - count - 1), (rownum - 1), 3, 3, input_sheet.cell((rownum - count), 3).value, styles.f2(input_sheet.cell((rownum - count), 3).value)) # severity level
					sheet.write_merge((rownum - count - 1), (rownum - 1), 5, 5, input_sheet.cell((rownum - count), 5).value, normal) # protocol
					sheet.write_merge((rownum - count - 1), (rownum - 1), 7, 7, input_sheet.cell((rownum - count), 7).value, normal) # name
					sheet.write_merge((rownum - count - 1), (rownum - 1), 8, 8, input_sheet.cell((rownum - count), 8).value, normal) # synopsis
					sheet.write_merge((rownum - count - 1), (rownum - 1), 9, 9, input_sheet.cell((rownum - count), 9).value, normal) # descr
					sheet.write_merge((rownum - count - 1), (rownum - 1), 10, 10, input_sheet.cell((rownum - count), 10).value, normal) # solution
					sheet.write_merge((rownum - count - 1), (rownum - 1), 11, 11, input_sheet.cell((rownum - count), 11).value, normal) # also
					sheet.write_merge((rownum - count - 1), (rownum - 1), 12, 12, input_sheet.cell((rownum - count), 12).value, normal) # output
				if cve_count!=0:
					sheet.write_merge((rownum - cve_count - 1), (rownum - 1), 1, 1, input_sheet.cell((rownum - cve_count), 1).value, normal) # cve
					cve_count=0
				if port_count!=0:
					sheet.write_merge((rownum - port_count - 1), (rownum - 1), 6, 6, input_sheet.cell((rownum - port_count), 6).value, normal) # port
					port_count=0
				if hostname_count!=0:
					sheet.write_merge((rownum - hostname_count - 1), (rownum - 1), 4, 4, input_sheet.cell((rownum - hostname_count), 4).value, normal) # hostname
					hostname_count=0

		set_width(sheet,wb)
		wb.save(filename[0:(len(filename)-13)]+".xls")
		print("Report ready")

wb = xlwt.Workbook()
wb.set_colour_RGB(0x21, 255, 101, 105)
wb.set_colour_RGB(0x22, 255, 153, 153)
wb.set_colour_RGB(0x23, 255, 192, 0)
wb.set_colour_RGB(0x24, 153, 255, 153)
wb.set_colour_RGB(0x25, 255, 255, 204)

format_and_paint(filename, wb)