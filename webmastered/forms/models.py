from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField()
    message = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message " + str(self.id)

    class Meta:
        verbose_name = "Contact Form Submission"
        verbose_name_plural = "Contact Form Submissions"
