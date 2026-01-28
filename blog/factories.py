import random
import factory
from .models import Post, Category
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: fake.user_name())
    email = factory.LazyAttribute(lambda x: fake.email())
    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda x: fake.sentence())
    slug = factory.LazyAttribute(lambda obj: fake.slug(obj.title))
    content = factory.LazyAttribute(lambda _: fake.text())
    published = factory.LazyAttribute(lambda x: random.choice([True, False]))

    @factory.lazy_attribute
    def category(self):
        categories = list(Category.objects.all())
        if categories:
            return random.choice(categories)
        return Category.objects.create(
            name=fake.word(),
            slug=fake.slug(),
            description=fake.text()
        )
    @factory.lazy_attribute
    def author(self):
        users = list(User.objects.all())
        if users:
            return random.choice(users)
        return UserFactory()