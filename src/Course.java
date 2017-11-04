import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.FileSystems;
import java.nio.file.Path;

@XmlRootElement
public class Course {
    Parent parents;
    String label;
    @XmlElement
    String description;
    String creditHours;
    String courseSectionInformation;
    String sectionRegistrationNotes;
    Section[] sections;

    public Parent getParents() {
        return parents;
    }

    public String getLabel() {
        return label;
    }

    public String getDescription() {
        return description;
    }

    public String getCreditHours() {
        return creditHours;
    }

    public String getCourseSectionInformation() {
        return courseSectionInformation;
    }

    public String getSectionRegistrationNotes() {
        return sectionRegistrationNotes;
    }

    public Section[] getSections() {
        return sections;
    }

    public static Course parseXML(String urlString) {
        URL url = null;
        Course course = null;
        try { url = new URL(urlString); } catch (MalformedURLException e) { }

        try {
            JAXBContext jaxbContext = JAXBContext.newInstance(Course.class);
            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            course = (Course) jaxbUnmarshaller.unmarshal(url);
        } catch (JAXBException e) {

        }

        return course;
    }

    public static void main(String args[]) {
        Course course = Course.parseXML("https://courses.illinois.edu/cisapp/explorer/schedule/2018/spring/CS/126.xml");
        System.out.println(course.getDescription());
    }
}
