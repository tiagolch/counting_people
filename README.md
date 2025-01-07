# 📊 Projeto de Contagem de Pessoas - Igreja

Este projeto é uma aplicação web desenvolvida em **Django** para auxiliar na contagem de participantes, visitantes, crianças e conversões durante as reuniões da igreja. A aplicação permite que os voluntários registrem as contagens, e os administradores possam visualizar e consolidar os dados com facilidade.

---

## 🚀 Funcionalidades

- **Registro de Contagens:**  
  Voluntários podem registrar contagens de pessoas, visitantes, crianças e conversões em cada reunião.  
  
- **Filtragem Avançada:**  
  A contagem pode ser filtrada por **data**, **localização**, **horário** e **status de validação** (validados ou não).  
  
- **Resumo Consolidado:**  
  A página de resumo apresenta um card consolidado com totais, permitindo copiar as informações com um clique para facilitar o envio via WhatsApp.  
  
- **Interface Intuitiva:**  
  Interface responsiva e estilizada usando **Bootstrap 5**.  

- **Administração de Dados:**  
  O administrador pode validar e consolidar contagens por meio de uma interface dedicada.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django (Python)  
- **Banco de Dados:** SQLite (Pode ser alterado para PostgreSQL)  
- **Frontend:** Bootstrap 5, HTML5, CSS3  
- **Scripts:** JavaScript (para copiar o resumo consolidado)  

---

## 📂 Estrutura do Projeto

```
contagem_pessoas/
│
├── core/                           # Aplicação principal
│   ├── migrations/                 # Migrations do banco de dados
│   ├── static/                     # Arquivos estáticos (CSS, JS, Imagens)
│   ├── templates/                  # Templates HTML
│   │   ├── resumo_contagem.html    # Página de resumo das contagens
│   ├── admin.py                    # Configuração do painel administrativo
│   ├── models.py                   # Modelos de dados
│   ├── views.py                    # Views (lógica do aplicativo)
│   └── urls.py                     # Rotas do aplicativo
│
├── main/                           # Configuração do projeto Django
│   ├── settings.py                 # Configurações do Django
│   ├── urls.py                     # URLs do projeto
│   └── wsgi.py                     # Configuração WSGI para deploy
│
├── db.sqlite3                      # Banco de dados SQLite
├── manage.py                       # Ferramenta de gerenciamento do Django
└── README.md                       # Documentação do projeto
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/contagem-pessoas.git
cd contagem-pessoas
```

### 2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados:
```bash
python manage.py migrate
```

### 5. Crie um superusuário (opcional, para acessar o painel admin):
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor:
```bash
python manage.py runserver
```

Acesse o projeto em:  
```
http://127.0.0.1:8000/
```

---

## 🔧 Configuração do Banco de Dados (opcional)

O projeto está configurado para usar **SQLite** por padrão. Caso deseje utilizar PostgreSQL, edite o arquivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📝 Modelos de Dados (Models)

### **Modelo Contagem**
```python
class Contagem(models.Model):
    reuniao = models.ForeignKey('Reuniao', on_delete=models.CASCADE)
    host_nome = models.CharField(max_length=100)
    total_pessoas = models.PositiveIntegerField()
    visitantes = models.PositiveIntegerField()
    criancas = models.PositiveIntegerField()
    conversoes = models.PositiveIntegerField()
    validado = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True)
```

### **Modelo Reuniao**
```python
class Reuniao(models.Model):
    localizacao = models.ForeignKey('Localizacao', on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
```

### **Modelo Localizacao**
```python
class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
```

---

## 🖥️ Página de Resumo das Contagens

A página de resumo exibe:  
- Tabela detalhada das contagens.  
- Filtros por data, localização, horário e validação.  
- Card consolidado com totais, com opção de copiar o resumo.  

---

## 🛡️ Segurança
- A aplicação conta com proteção contra CSRF (Cross-Site Request Forgery).  
- Apenas usuários autorizados podem validar e consolidar contagens.  

---

## 🧩 Melhorias Futuras
- Exportação de resumos em PDF ou Excel.  
- Integração com API para envio automático via WhatsApp.  
- Painel administrativo mais detalhado para acompanhamento das contagens.  

---

## 🤝 Contribuição

1. Faça um **fork** do projeto.  
2. Crie uma nova branch com a sua feature:  
   ```bash
   git checkout -b minha-feature
   ```  
3. Faça commit das suas alterações:  
   ```bash
   git commit -m 'Adiciona nova feature'
   ```  
4. Envie para o branch principal:  
   ```bash
   git push origin minha-feature
   ```  
5. Abra um Pull Request! 🚀  

---

## 📄 Licença
Este projeto está sob a licença **MIT**.  

Se precisar de mais informações ou ajustes no projeto, estou à disposição! 😊

