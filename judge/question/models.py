from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=250)
    test_count = models.PositiveIntegerField()
    statement = models.TextField()
    class Meta:
       verbose_name = "Question"
       verbose_name_plural = "Questions"

class Test(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="question",
    )
    title = models.CharField(max_length=250)
    # input_file_<question_id>_<test_id>
    input_file = models.FilePathField(
        path="test",
        match="input_file*"
    )
    output_file = models.FilePathField(
        path="test",
        match="output_file*"
    )
    class Meta:
       verbose_name = "Test"
       verbose_name_plural = "Tests"


 