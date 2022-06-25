from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=f'{faker_ru.last_name()} {faker_ru.first_name()} {faker_ru.middle_name()}',
        company=faker_ru.job(),
        email=faker_ru.email(),
        text_of_appeal=faker_ru.paragraph(nb_sentences=5, variable_nb_sentences=False),
    )
