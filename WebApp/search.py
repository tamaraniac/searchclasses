import requests
from xml.etree.ElementTree import fromstring, ElementTree
import xml.dom.minidom
from .Class import Class
from .functions import timeConvert, inString


def search(term, year, subjectID, courseNum, daysOfTheWeek, earliestTime, latestTime, breakStart, breakEnd, gened):

    earliestTime = timeConvert(earliestTime)
    latestTime = timeConvert(latestTime)
    breakStart = timeConvert(breakStart)
    breakEnd = timeConvert(breakEnd)
    responseYear = None
    term_dic = {'spring': 1, 'summer': 5, 'fall': 8, 'winter': 0}
    responseSubject = None
    responseClass = None
    courseList = []
    classList = []



    response = requests.get("https://courses.illinois.edu/cisapp/explorer/schedule.xml")
    root = fromstring(response.content)
    List = root.findall('./calendarYears/calendarYear')
    # search for the year in all the years
    for element in List:
        if element.get('id') == year:
            responseYear = requests.get(element.attrib['href'])
            break

    if responseYear == None:
        raise KeyError('The year of search doesn\'t exist')

    rootYear = fromstring(responseYear.content)
    termList = rootYear.findall('./terms/term')
    # search for the term in that year
    for element in termList:
        if element.attrib['id'].endswith(str(term_dic[term])):
            responseSubject = requests.get(element.attrib['href'])
            break

    if responseSubject == None:
        raise KeyError('The term of search doesn\'t exist')

    rootSubjects = fromstring(responseSubject.content)
    subjectList = rootSubjects.findall('./subjects/subject')

    # if not looking for specific subject, the list of classes should be all classes of all subjects
    if subjectID != None:
        for element in subjectList:
            if element.attrib['id'] == subjectID:
                responseClass = requests.get(element.attrib['href'])
                break
        if responseClass == None:
            raise KeyError('The subject of search doesn\'t exist')
        rootClass = fromstring(responseClass.content)

        # find course according to courseNum
        if courseNum != None:
            for course in rootClass.findall('./courses/course'):
                if course.get('id') == courseNum:
                    courseList.append(course)
        # if there is no courseNum require, put all courses in there
        else:
            courseList = rootClass.findall('./courses/course')

        if courseList == []:
            raise KeyError('The course number of search doesn\'t exist')

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
                if daysOfTheWeek != None and daysOfTheWeek != '':
                    sectionTime = sectionRoot.find('./meetings/meeting/daysOfTheWeek')
                    if sectionTime != None:
                        sectionTime = sectionTime.text.strip()
                        if not inString(sectionTime, daysOfTheWeek):
                            qualified = False
                    else:
                        qualified = False

                # start and end time
                start = sectionRoot.find('./meetings/meeting/start')
                end = sectionRoot.find('./meetings/meeting/end')

                # filter according to earliest start time
                if earliestTime != None:
                    if qualified and start != None and start.text[:2].isnumeric():
                        start1 = timeConvert(start.text.strip())
                        if start1 < earliestTime:
                            qualified = False
                    else:
                        qualified = False

                # filter according to Latest start time
                if latestTime != None:
                    if qualified and end != None and end.text[:2].isnumeric():
                        end1 = timeConvert(end.text.strip())
                        if end1 > latestTime:
                            qualified = False
                    else:
                        qualified = False

                # Break time
                if breakStart != None and breakEnd != None:
                    if qualified and start != None and end != None \
                        and start.text[:2].isnumeric() and end.text[:2].isnumeric():
                        start2 = timeConvert(start.text.strip())
                        end2 = timeConvert(end.text.strip())
                        if (start2 <= breakStart and end2 > breakStart) \
                            or (start2 > breakStart and end2 < breakEnd):
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


    
    return classList
