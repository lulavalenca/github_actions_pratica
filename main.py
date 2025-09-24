#!/usr/bin/env python3
"""
Script principal para prática de GitHub Actions
Equivalente ao código Go do professor
"""

import json
import csv
from datetime import datetime
import os
import sys

def generate_user_data(num_users=10):
    """Gera dados de usuários para teste"""
    users = []
    for i in range(num_users):
        user = {
            "id": i + 1,
            "name": f"User {i+1}",
            "email": f"user{i+1}@example.com",
            "created_at": datetime.now().isoformat(),
            "active": True
        }
        users.append(user)
    return users

def save_to_json(data, filename="users.json"):
    """Salva dados em JSON"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Dados salvos em {filename}")

def save_to_csv(data, filename="users.csv"):
    """Salva dados em CSV"""
    if data:
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Dados salvos em {filename}")

def main():
    """Função principal"""
    print("🚀 Iniciando GitHub Actions Prática com Python!")
    
    # Gerar dados de exemplo
    users = generate_user_data(5)
    
    # Salvar em diferentes formatos
    save_to_json(users, "users.json")
    save_to_csv(users, "users.csv")
    
    # Mostrar informações do sistema
    print(f"📋 Python version: {sys.version}")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"👤 Usuários gerados: {len(users)}")
    print(f"📄 Arquivos gerados: users.json, users.csv")
    print("🎉 Prática concluída com sucesso!")

if __name__ == "__main__":
    main()