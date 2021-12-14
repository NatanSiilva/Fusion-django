from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexView(TestCase):
	def setUp(self):
		self.datas = {
			'nome': 'Teste',
			'email': 'contato@gmail.com',
			'mensagem': 'Teste de mensagem',
			'assunto': 'Teste de assunto'
		}

		self.client = Client()

	def test_form_valid(self):
		request = self.client.post(reverse_lazy('index'), self.datas)
		self.assertEqual(request.status_code, 302)

	def test_form_invalid(self):
		self.datas['nome'] = ''
		request = self.client.post(reverse_lazy('index'), self.datas)
		self.assertEqual(request.status_code, 200)