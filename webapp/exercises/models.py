from django.db import models


class Lists(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Lists'


class Dictionaries(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Dictionaries'


class Tuples(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Tuples'


class Sets(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Sets'


class StringManipulation(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'String_manipulation'


class IndexingAndSlicing(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Indexing_and_Slicing'


class MutableAndImutableTypes(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Mutable_and_Imutable_types'


class DataTypes(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Data_types'


class MethodsOfTypes(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Methods_of_types'


class Comprehension(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Comprehension'


class Exceptions(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Exceptions'


class LocalAndGlobalScope(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Local_and_global_scope'


class Closures(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Closures'


class ShortCircuitEvaluation(models.Model):
    exercise_text = models.TextField(db_column='exercise')

    class Meta:
        db_table = 'Short_circuit_evaluation'
