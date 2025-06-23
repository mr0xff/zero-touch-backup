# ZeroTouchBackup

Backup automático de bancos de dados PostgreSQL com envio por email — totalmente autônomo, multiplataforma e leve.

---

## Visão Geral

**ZeroTouchBackup** foi criado para automatizar o processo diário de backup de bancos de dados PostgreSQL, eliminando tarefas manuais.  
Funciona como serviço no **Linux** (`systemd`) e também no **Windows** (via `pywin32`).

---

## Funcionalidades

- Executa como serviço de sistema (Linux/Windows)
- Envia backups por email com autenticação segura (TLS)
- Mantém log de eventos e controle de arquivos enviados
- Resistente a falhas (reinício automático no Linux)

---

## Instalação (Linux)

```bash
# Requisitos: Python 3.x instalado

# Copie para /opt
sudo cp -r ZeroTouchBackup /opt/bot

# Permissões
sudo chmod +x /opt/bot/sendermail.py

# Ative o serviço systemd
sudo cp /opt/bot/bot.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable --now bot.service
