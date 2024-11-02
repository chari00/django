

# Create your models here.

# ----------------------------
# Introduction to Django Models
# ----------------------------

# Django Models are Python classes that define the structure of your data.
# Each class represents a database table, and the fields of the class correspond to columns in that table.

# Let's start by defining a basic Django model for a 'Book'. This model will store information about books 
# such as the title, author, publication date, and whether it's available.

from django.db import models

# ----------------------------
# Example: Defining a Simple Model
# ----------------------------

# Here is an example of a basic model class. It represents a 'Book' in the system:
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (up to 100 characters)
    author = models.CharField(max_length=100)  # Author's name
    published_date = models.DateField()  # Publication date of the book
    is_available = models.BooleanField(default=True)  # Availability of the book

    def __str__(self):
        return f"{self.title} by {self.author}"


# ----------------------------
# Example: Working with Fields and Options
# ----------------------------

# Django models provide various field types to define your data:
# CharField is used for short text (e.g., names), DateField for dates, BooleanField for true/false values.

# In this example, we add more complexity to the model by including additional fields and options.

class LibraryMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    membership_start = models.DateField()  # Date when the member joined the library
    email = models.EmailField()  # Email field with built-in validation
    books_borrowed = models.IntegerField(default=0)  # Number of books borrowed (default is 0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Explanation:
# - CharField defines short text fields.
# - EmailField automatically validates that the email is in the correct format.
# - IntegerField stores whole numbers, like the count of books a member has borrowed.

# ----------------------------
# Extra Example: Using Model Methods
# ----------------------------

# Models can also have methods that allow us to work with the data in interesting ways.
# Let's add a method to the 'Book' model to check if it's a new release.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def is_new_release(self):
        from datetime import date
        # Consider the book new if it was published within the last year.
        return (date.today() - self.published_date).days <= 365

    def __str__(self):
        return f"{self.title} by {self.author}"

# Now, when you work with a Book instance, you can call `is_new_release()` to check if it's a new book.

# ----------------------------
# Conclusion
# ----------------------------

# Django models are powerful tools that allow developers to define the structure of the data in their applications.
# They abstract away the need for SQL queries, making it easier to interact with databases in a Pythonic way.
# By using models, you can handle everything from data validation to database migrations, all while keeping your code clean and maintainable.