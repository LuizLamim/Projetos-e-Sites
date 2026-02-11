import json
from steampy.client import SteamClient
from steampy.utils import GameOptions

class SteamLevelUpBot:
    def __init__(self, api_key, username, password, steam_guard_file):
        self.api_key = api_key
        self.username = username
        self.password = password

        with open(steam_guard_file, 'r') as f:
            secrets = json.load(f)
            self.shared_secret = secrets['shared_secret']
            self.identity_secret = secrets['identity_secret']
            
        self.client = SteamClient(self.api_key)

    def login(self):
        """Realiza o login e configura as credenciais do Steam Guard"""
        print(f"[*] Tentando logar na conta: {self.username}...")
        
        try:
            self.client.login(self.username, self.password, self.shared_secret)
            
            if self.client.is_session_alive():
                print("[+] Login realizado com sucesso!")
                return True
            else:
                print("[-] Falha ao verificar sessão.")
                return False
                
        except Exception as e:
            print(f"[-] Erro crítico no login: {e}")
            return False
        
    def get_inventory_summary(self):
        """
        Busca o inventário de itens da Comunidade Steam (Cartas, Gemas, BGs)
        Game ID 753 = Steam
        Context ID 6 = Community Items
        """
        if not self.client.is_session_alive():
            print("[-] Sessão expirada. Faça login novamente.")
            return

        print("[*] Buscando inventário...")
        # O ID 753 é o AppID da Steam (onde vivem as cartas)
        # O Context 6 são itens de troca/comunidade
        inventory = self.client.get_my_inventory(game=GameOptions.STEAM, merge=True)
        
        total_items = len(inventory)
        gems_count = 0
        cards_count = 0