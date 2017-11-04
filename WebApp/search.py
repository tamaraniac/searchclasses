import requests
from xml.etree.ElementTree import fromstring, ElementTree
import xml.dom.minidom
from Class import Class

# Supposed inputs
year = 2018
term = 'spring'
subjectID = 'CS' #can be None
courseNum = '225'
gened = 'HA'
daysOfTheWeek = 'MWF' # might be passed in differently (as boolean)



responseYear = None
term_dic = {'spring': 1, 'summer': 5, 'fall': 8, 'winter': 0}
responseSubject = None
responseClass = None
courseList = []
classList = []

def inString(small, big):
    for char in small:
        if char not in big:
            return False
    return True


response = requests.get("https://courses.illinois.edu/cisapp/explorer/schedule.xml")
root = fromstring(response.content)
List = root.findall('./calendarYears/calendarYear')
# search for the year in all the years
for element in List:
    if element.attrib['id'] == str(year):
        responseYear = requests.get(element.attrib['href'])
        break

rootYear = fromstring(responseYear.content)
termList = rootYear.findall('./terms/term')
# search for the term in that year
for element in termList:
    if element.attrib['id'].endswith(str(term_dic[term])):
        responseSubject = requests.get(element.attrib['href'])
        break
rootSubjects = fromstring(responseSubject.content)
subjectList = rootSubjects.findall('./subjects/subject')

# if not looking for specific subject, the list of classes should be all classes of all subjects
if subjectID != None:
    for element in subjectList:
        if element.attrib['id'] == subjectID:
            responseClass = requests.get(element.attrib['href'])
            break
    rootClass = fromstring(responseClass.content)

    # find course according to courseNum
    if courseNum != None:
        for course in rootClass.findall('./courses/course'):
            if course.get('id') == courseNum:
                courseList.append(course)
    # if there is no courseNum require, put all courses in there
    else:
        courseList = rootClass.findall('./courses/course')

    for course in courseList:
        responseIndiClass = requests.get(course.get('href'))
        tempRoot = fromstring(responseIndiClass.content)
        tempClass = Class(tempRoot)
        # add sections to each class
        for section in tempRoot.findall('./sections/section'):
            responseSection = requests.get(section.get('href'))
            sectionRoot = fromstring(responseSection.content)

            #-------filter out sections-------
            # days of week
            qualified = True
            if daysOfTheWeek != None:
                sectionTime = sectionRoot.find('./meetings/meeting/daysOfTheWeek').text.strip()
                if not inString(sectionTime, daysOfTheWeek):
                    qualified = False



            if qualified:
                tempClass.add_section(sectionRoot)

        classList.append(tempClass)



## put in gened requirement here
else:
    for element in subjectList:
        responseClass = requests.get(element.attrib['href'])
        rootClass = fromstring(responseClass.content)
        courseList += rootClass.findall('./courses/course')



# testing
for course in classList:
    print (course.clas.get('id'), course.clas.find('./label').text)
    for section in course.sectionList:
        print('section:', section.find('./sectionNumber').text)
