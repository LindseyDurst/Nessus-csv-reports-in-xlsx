#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt

xlwt.add_palette_colour("critical", 0x21)
xlwt.add_palette_colour("high", 0x22)
xlwt.add_palette_colour("medium", 0x23)
xlwt.add_palette_colour("low", 0x24)

#----------------------------------------------------------
def f(str):
	F_STYLES = {u"Critical" : style_critical,
				u"High": style_high,
				u"Low": style_low,
				u"Medium": style_medium,
				u"None": style_none}

	if F_STYLES.get(str):
		return F_STYLES.get(str)
	else:
		return style
#----------------------------------------------------------------
def f2(str):
	F_STYLES2 = {u"Critical" : style_critical2,
				u"High": style_high2,
				u"Low": style_low2,
				u"Medium": style_medium2,
				u"None": style_none2}
	if F_STYLES2.get(str):
		return F_STYLES2.get(str)
	else:
		return style2
#---------------------------------------
style = xlwt.XFStyle()

head_style = xlwt.XFStyle()

font=xlwt.Font()
font.bold=True
font.height = 220
font.name = 'Calibri'
head_style.font=font

center = xlwt.Alignment()
center.horz = xlwt.Alignment.HORZ_CENTER
center.vert = xlwt.Alignment.VERT_CENTER
head_style.alignment=center
head_style.alignment.wrap = 1

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']
head_style.font.colour_index = xlwt.Style.colour_map['white']
head_style.pattern = pattern

borders = xlwt.Borders()
borders.left = xlwt.Borders.DOUBLE
borders.right = xlwt.Borders.DOUBLE
borders.top = xlwt.Borders.DOUBLE
borders.bottom = xlwt.Borders.DOUBLE
head_style.borders = borders
#----------------------------------------------------------------------
middle_style = xlwt.XFStyle()

middle_style.alignment=center
middle_style.alignment.wrap = 1
#----------------------------------------------------------------------
middle_head_style = xlwt.XFStyle()
font=xlwt.Font()
font.bold=True
font.name = 'Calibri'
middle_head_style.font=font

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']
middle_head_style.pattern=pattern

#----------------------------------------------------------------------
style_critical = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['critical']
style_critical.pattern = pattern
style_critical.alignment=center
style_critical.alignment.wrap = 1
style_critical.font = font

style_high = xlwt.XFStyle()
pattern2 = xlwt.Pattern()
pattern2.pattern = xlwt.Pattern.SOLID_PATTERN
pattern2.pattern_fore_colour = xlwt.Style.colour_map['high']
style_high.pattern = pattern2
style_high.alignment=center
style_high.alignment.wrap = 1
style_high.font = font

style_low = xlwt.XFStyle()
pattern3 = xlwt.Pattern()
pattern3.pattern = xlwt.Pattern.SOLID_PATTERN
pattern3.pattern_fore_colour = xlwt.Style.colour_map['low']
style_low.pattern = pattern3
style_low.alignment=center
style_low.alignment.wrap = 1
style_low.font = font

style_none = xlwt.XFStyle()
pattern4 = xlwt.Pattern()
pattern4.pattern = xlwt.Pattern.SOLID_PATTERN
pattern4.pattern_fore_colour = xlwt.Style.colour_map['white']
style_none.pattern = pattern4
style_none.alignment=center
style_none.alignment.wrap = 1
style_none.font = font

#=======================================================================================================================
style_critical2 = xlwt.XFStyle()
pattern10 = xlwt.Pattern()
pattern10.pattern = xlwt.Pattern.SOLID_PATTERN
pattern10.pattern_fore_colour = xlwt.Style.colour_map['critical']
style_critical2.alignment=center
font=xlwt.Font()
font.bold=True
font.height = 220
font.name = 'Calibri'
style_critical2.font=font
style_critical2.pattern = pattern10

style_high2 = xlwt.XFStyle()
pattern11 = xlwt.Pattern()
pattern11.pattern = xlwt.Pattern.SOLID_PATTERN
pattern11.pattern_fore_colour = xlwt.Style.colour_map['high']
style_high2.alignment=center
font=xlwt.Font()
font.bold=True
font.height = 220
style_high2.font=font
font.name = 'Calibri'
style_high2.pattern = pattern11

style_medium2 = xlwt.XFStyle()
pattern12 = xlwt.Pattern()
pattern12.pattern = xlwt.Pattern.SOLID_PATTERN
pattern12.pattern_fore_colour = xlwt.Style.colour_map['medium']
style_medium2.alignment=center
font=xlwt.Font()
font.bold=True
font.height = 220
style_medium2.font=font
font.name = 'Calibri'
style_medium2.pattern = pattern12

style_low2 = xlwt.XFStyle()
pattern13 = xlwt.Pattern()
pattern13.pattern = xlwt.Pattern.SOLID_PATTERN
pattern13.pattern_fore_colour = xlwt.Style.colour_map['low']
style_low2.alignment=center
font=xlwt.Font()
font.bold=True
font.height = 220
style_low2.font=font
font.name = 'Calibri'
style_low2.pattern = pattern13

style_none2 = xlwt.XFStyle()
pattern14 = xlwt.Pattern()
style_none2.alignment=center
font=xlwt.Font()
font.bold=False
font.height = 220
style_none2.font=font
font.name = 'Calibri'
style_none2.pattern = pattern14

style2 = xlwt.XFStyle()

