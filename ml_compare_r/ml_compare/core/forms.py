from django import forms

from ml_compare.core.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'doc_type',)
        #doct_t = TypeForm
