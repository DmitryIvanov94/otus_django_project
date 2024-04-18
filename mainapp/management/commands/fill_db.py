from mainapp.models import CategoryCourse, Course, Lesson, Schedule
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        print('Clear db...')
        Schedule.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        CategoryCourse.objects.all().delete()

        print('Create_superuser...')
        User = get_user_model()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin54321')
        admin.save()

        print('Create categories...')
        category_1 = CategoryCourse.objects.create(name='Development', description='For developers')
        category_2 = CategoryCourse.objects.create(name='Software tester', description='For QA')

        print('Create courses...')
        course_1 = Course.objects.create(name='Django developer', description='You will good django developer',
                                         category=category_1)
        course_2 = Course.objects.create(name='Python developer', description='You will good python developer',
                                         category=category_2)

        print('Create lessons...')
        lesson_1_django = Lesson.objects.create(name='Lesson 1 start Django', course=course_1)
        lesson_2_django = Lesson.objects.create(name='Lesson 2', course=course_1)
        lesson_1_python = Lesson.objects.create(name='Lesson 1', course=course_2)

        print('Create schedules...')
        Schedule.objects.create(date='2025-01-01 00:00', lesson=lesson_1_django)
        Schedule.objects.create(date='2025-01-01 00:00', lesson=lesson_2_django)
        Schedule.objects.create(date='2025-01-01 00:00', lesson=lesson_1_python)

        print('Create teachers...')
        teacher_1 = User.objects.create_user('otus', 'otus@otus.com', 'otus54321')
        teacher_1.first_name = 'Teacher'
        teacher_1.last_name = 'Lectorovich'
        teacher_1.save()
        course_1.teachers.add(teacher_1)
        course_2.teachers.add(admin)
        course_1.save()
        course_2.teachers.add(teacher_1)
        course_2.teachers.add(admin)
        course_2.save()

        self.stdout.write(
            self.style.SUCCESS('Done')
        )
