from django.test import TestCase
from course.models import Course
from course.models import Course, Branch, Category, Contact

class CourseModelTest(TestCase):

    def setUp(self):
        category = Category.objects.create(name="Testcategory", imgpath="Testimage2")
        course = Course.objects.create(name="Testname", description="Testdescription", logo="Testlogo", category=category)
        contact = Contact.objects.create(contact_type=1, value="Testvalue", course=course)
        branch = Branch.objects.create(latitude="Testlatitude", longitude="Testlongitude", address="Testaddress", course=course)
  
    def test_category(self):
        category = Category.objects.order_by().first()
        title_name = category.name
        title_image = category.imgpath
        self.assertEqual(title_name, 'Testcategory')
        self.assertEqual(title_image, 'Testimage2')

    def test_course(self):
        course = Course.objects.order_by().first()
        title_name = course.name
        title_description = course.description
        title_logo = course.logo
        self.assertEquals(title_name, 'Testname')
        self.assertEquals(title_description, 'Testdescription')
        self.assertEquals(title_logo, 'Testlogo')

    def test_contact(self):
        contact = Contact.objects.order_by().first()
        title_contact = contact.value
        self.assertEqual(title_contact, 'Testvalue')

    def test_branch(self):
        branch = Branch.objects.order_by().first()
        title_latitude = branch.latitude
        title_longitude = branch.longitude
        title_address = branch.address
        self.assertEqual(title_latitude, 'Testlatitude')
        self.assertEqual(title_longitude, 'Testlongitude')
        self.assertEqual(title_address, 'Testaddress')