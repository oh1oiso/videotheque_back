# Utiliser l'image Python officielle
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le contenu actuel dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Flask écoute
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "api.py"]
