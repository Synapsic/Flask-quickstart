# Démarrage rapide avec Flask

Flask est un framework backend pour python, extensible, flexible et très facile à prendre en main. Il s'intègre sans problème avec le protocole d'authentification de Synapse et est très efficace pour le design d'API RESTful, tout en ayant l'avantage d'être interpolable avec des technologies écrites en python, comme la majorité des IA modernes. Ce kit de démarrage inclut un front-end `Vanilla`, ce qui correspond à des fichiers HTML, CSS et JavaScript simples, sans framework ou librairie préfaite.

## Commencer

Premièrement, il vous faudra récupérer vos identifiants d'Application Synapse sur le portail développeur (SDK) ou via un ticket sur le serveur discord de Synapse. Une fois la manipulation effectuée, assignez à `SYNAPSE_ID` et `SYNAPSE_SECRET` dans un fichier `.env` (qui définit les variables d'environnement) les identifiants obtenus pendant l'étape précédente.

```bash
SYNAPSE_ID=<your_synapse_client_id>
SYNAPSE_SECRET=<your_synapse_client_secret>
```

Ensuite, récupérez les fichiers de [Synapsic/Vanilla-front](https://github.com/Synapsic/Vanilla-front) et placez-les dans le dossier `public/`. Il ne vous reste plus qu'à installer les dépendances et à lancer le projet ! Si c'est exécuté localement, vous trouverez votre application à l'adresse [`localhost:8080`](https://localhost:8080/).

### Avec poetry

```bash
pip install poetry
poetry install
python main.py
```

### Avec pip

```bash
pip install -r requirements.txt
python main.py
```