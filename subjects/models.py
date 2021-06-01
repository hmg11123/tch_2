from django.db import models


class Subject(models.Model):

    CHOICE_EASY = "easy"
    CHOICE_USUALLY = "usually"
    CHOICE_DIFFICULT = "difficult"

    CHOICE_DIFFICULTY = (
        (CHOICE_EASY, "EASY"),
        (CHOICE_USUALLY, "USUALLY"),
        (CHOICE_DIFFICULT, "DIFFICULT"),
    )

    name = models.CharField(max_length=100)
    subject_difficulty = models.CharField(choices=CHOICE_DIFFICULTY, max_length=40)
    
    class Meta:
        verbose_name_plural = "과목 관리"
    
    def __str__(self):
        return self.name