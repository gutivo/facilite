from django import forms
from cadastros.models import Campo

class SeuFormulario(forms.Form):
    PODER_CHOICES = [
       ('PODER LEGISLATIVO', 'PODER LEGISLATIVO'),
       ('PODER EXECUTIVO', 'PODER EXECUTIVO'),
       ('FUNDO MUNICIPAL DE SAÚDE', 'FUNDO MUNICIPAL DE SAÚDE'),
       ('FUNDO MUNICIPAL DE ASSISTÊNCIA SOCIAL', 'FUNDO MUNICIPAL DE ASSISTÊNCIA SOCIAL'),
       ('FUNDO MUNICIPAL DO MEIO AMBIENTE', 'FUNDO MUNICIPAL DO MEIO AMBIENTE'),
    ]
    GENERO_CHOICES = [
       ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
    ]
    TIPOREF_CHOICES = [
       ('Prestação de serviço', 'Prestação de serviço'),
        ('Prestação de fornecimento', 'Prestação de fornecimento'),
    ]
    MODALIDADE_CHOICES = [
       ('Dispensa', 'Dispensa'),
        ('Inexigibilidade', 'Inexigibilidade'),
    ]
    INCISO_CHOICES = [
       ('I', 'I'),
        ('II','II'),
        ('III','III'),
        ('III, linear A','III, linear A'),
        ('III, linear B','III, linear B'),
        ('III, linear C','III, linear C'),
        ('III, linear D','III, linear D'),
        ('III, linear E','III, linear E'),
        ('III, linear F','III, linear F'),
        ('III, linear G','III, linear G'),
        ('III, linear H','III, linear H'),
        ('IV','IV'),
        ('V','V'),
    ]
    # Cidade
    campo = forms.ModelChoiceField(queryset=Campo.objects.all(), label="Órgão/Empresa")
    poder = forms.CharField(label='Tipo de Poder',widget=forms.Select(choices=PODER_CHOICES))
    tipopro = forms.CharField(label='Modalidade',widget=forms.Select(choices=MODALIDADE_CHOICES))
    tipoinciso = forms.CharField(label='Inciso',widget=forms.Select(choices=INCISO_CHOICES))
    # Solicitação
    
    gen = forms.CharField(label='Tipo de tratamento',widget=forms.Select(choices=GENERO_CHOICES))
    obj1 = forms.CharField(label='Objeto', max_length=245)
    descr1 = forms.CharField(label='Descrição', max_length=245)
    descr2 = forms.CharField(label='Tipo de processo',widget=forms.Select(choices=TIPOREF_CHOICES))
    nupros = forms.CharField(label='N° Dis/Inex', max_length=10)
    nuproto = forms.CharField(label='N° Processo', max_length=10)
    anopro = forms.CharField(label='Ano Processo', max_length=10)
    pc = forms.CharField(label='Prazo', max_length=50)
    dot = forms.CharField(label='Dotação Orçamentária', max_length=150)
    fonte = forms.CharField(label='Fonte de recurso', max_length=10)
    cnpjx = forms.CharField(label='CNPJ VENCEDOR', max_length=20)
    vt = forms.CharField(label='Valor Total Vencedor-(número e por extenso)', max_length=240)
    vtm = forms.CharField(label='Valor Total Parametrização-(número e por extenso)', max_length=240)
    data1 = forms.DateField(label='Data Solicitação')
    data2 = forms.DateField(label='Data Publicação de Aviso')
    data3 = forms.DateField(label='Data Termo de Referencia')
    data4 = forms.DateField(label='Data Estudo Técnico Preliminar')
    data5 = forms.DateField(label='Data Autorização')
    data6 = forms.DateField(label='Data Despacho')
    data7 = forms.DateField(label='Data Certidão')
    data8 = forms.DateField(label='Data R.C.L')
    data9 = forms.DateField(label='Data Ato Declaratório')
    data10 = forms.DateField(label='Data Parecer C.I')
