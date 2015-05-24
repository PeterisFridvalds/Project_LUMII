from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

class Tezaurs(models.Model):
    Header = EmbeddedModelField('DataHeader', null=True)
    ID = models.CharField(max_length = 2, null=True)
    Senses = ListField(EmbeddedModelField('DataSenses', null=True), null=True)
    Phrases = ListField(EmbeddedModelField('DataPhrases', null=True), null=True)
    Derivatives = ListField(EmbeddedModelField('DataHeader', null=True), null=True)
    Sources = ListField(null=True)

class DataHeader(models.Model):
    Lemma = models.TextField(null=True)
    Pronunciation = ListField(null=True)
    Gram = EmbeddedModelField('DataGram', null=True)

class DataGram(models.Model):
    Paradigm = ListField(null=True)
    AltLemmas = ListField(EmbeddedModelField('DataAltLemmas', null=True), null=True)
    Flags = ListField(null=True)
    Leftovers = ListField(ListField(null=True), null=True)
    Original = models.TextField(null=True)

class DataAltLemmas(models.Model):
    Lemma = models.TextField(null=True)
    Paradigm = ListField(null=True)
    Flags = ListField(null=True)

class DataSenses(models.Model):
    SenseID = models.CharField(max_length = 2, null=True)
    Gram = EmbeddedModelField('DataGram', null=True)
    Gloss = models.TextField(null=True)
    Examples = ListField(EmbeddedModelField('DataPhrase', null=True), null=True)
    Senses = ListField(EmbeddedModelField('DataSenses', null=True), null=True)
    
class DataPhrase(models.Model):
    Text = models.TextField(null=True)
    Gram = EmbeddedModelField('DataGram', null=True)
    Senses = ListField(EmbeddedModelField('DataSenses', null=True), null=True)

class DataPhrases(models.Model):
    Phrase = EmbeddedModelField('DataPhrase', null=True)
