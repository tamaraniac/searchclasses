import schedule
import time

from searchLocal import search


def job():

    classList = search('spring', '2018', 'AE', '482', None, \
                       None, None, None, None, None)

    # testing
    for course in classList:
        print (course.clas.get('id'), course.clas.find('./label').text)
        for section in course.sectionList:
            if section.find('./sectionNumber') != None:
                print('section:', section.find('./sectionNumber').text, 'status:', section.find('./enrollmentStatus').text)

schedule.every(18).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
