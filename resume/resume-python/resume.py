from xml.dom.minidom import parse, parseString

def getTag(node, tagName):
	startTag = '<%s>' % tagName
	endTag = '</%s>' % tagName
	emptyTag = '<%s/>' % tagName
	xmlLine = node.getElementsByTagName(tagName)[0].toxml()
	tagText = xmlLine.replace(startTag,'').replace(endTag,'').replace(emptyTag,'')
	#tagText = tagText.rstrip(' ').lstrip(' ').rstrip('\r\n')
	tagText = tagText.strip()
	return tagText
	

class asciiWritter:
	def resumeHeader(self): #Resume
		print ""
		print "[[Mayel Espino's Resume]]"
		print ""
	def resumeFooter(self):
		print "================================================================================"
	def experienceHeader(self):
		print "---[Experience]".ljust(150,'-')
	def experienceRow(self,company, projects, role,responsabilities,tools,description,period,location):
		if company == '':
			return
		print ">Company: ", company
		print "| Location: ", location
		print "| Projects:", projects
		print "| Role: ", role
		print "| Responabilities: ",responsabilities
		print "| Tools: ",tools
		print "| Description: ",description
		print "| Period of employment: ", period
		print ".".ljust(150,'.')
	def experienceFooter(self):
		print " "
	def skillsHeader(self): #Skills
		pass
	def skillsRow(self):
		pass
	def skillsFooter(self):
		pass
	def summaryHeader(self): #Summary
		pass
	def summaryRow(self):
		pass
	def summaryFooter(self):
		pass
	def educationHeader(self): #Education
		pass
	def skillsHeader(self): #Skills
		print "---[Skills]".ljust(150,'-')
	def skillsRow(self,name,level,years,note):
		if name == '':
			return
		print '>',name.ljust(40,' '),'|',level.ljust(10,' '),'|',years.ljust(5,' ')
		if note != '':
			print '|',note.ljust(80,' ')
	def awardsHeader(self): #Awards
		pass

write = asciiWritter()

dom = parse("resume.xml" )

write.resumeHeader()
write.experienceHeader()

for node in dom.getElementsByTagName('position'):
	company = getTag(node, 'company')
	projects = getTag(node,'projects')
	role = getTag(node,'role')
	responsabilities = getTag(node,'responsabilities')
	tools = getTag(node,'tools')
	description = getTag(node,'description')
	period = getTag(node,'period')
	location = getTag(node,'location')
	write.experienceRow(company, projects, role,responsabilities,tools,description,period,location)
write.experienceFooter()

write.skillsHeader()
for node in dom.getElementsByTagName('skill'):
	name = getTag(node,'name')
	level = getTag(node,'level')
	years = getTag(node, 'years')
	note = getTag(node, 'note')
	write.skillsRow(name,level,years,note)

#for node in dom.getElementsByTagName('summary'):
#	item = getTag('item')
write.resumeFooter()