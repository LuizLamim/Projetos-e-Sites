# Diretrizes do Projeto: Projetos e Sites

Este arquivo define as convenções, padrões e mandatos para o desenvolvimento e manutenção deste repositório, que abrange utilitários Python, bots de automação e protótipos web.

## 🎯 Escopo do Projeto
Uma coleção multidisciplinar de ferramentas e sites, focada em:
- **Automação:** Bots para Discord e Steam.
- **Matemática e Ciência:** Utilitários de cálculo (potência, raiz cúbica, coeficiente angular) e simulações (partículas).
- **Web Development:** Landing pages responsivas e portfólios utilizando HTML5 e Vanilla CSS.
- **Banco de Dados:** Exemplos de persistência com SQLite.

## 🛠️ Stack Tecnológica
- **Linguagem Principal:** Python 3.x
- **Interfaces Gráficas:** Tkinter
- **Bibliotecas de Automação:** `discord.py`, `steampy`
- **Frontend:** HTML5, CSS3 (Preferência por Vanilla CSS)
- **Banco de Dados:** SQLite3

## 📏 Convenções de Código

### Python
- **Idioma:** Comentários e documentação devem ser escritos em **Português (BR)**.
- **Estilo:** Seguir o PEP 8.
- **Robustez:** Sempre incluir blocos `try/except` para capturar erros de input ou falhas de conexão em scripts de rede/automação.
- **Modularidade:** Preferir a criação de funções ou classes reutilizáveis em vez de scripts lineares longos.

### Web (HTML/CSS)
- **Estilo:** Priorizar CSS puro (Vanilla CSS) para manter a leveza.
- **Responsividade:** Todos os arquivos HTML devem ser responsivos (Mobile First ou uso de Media Queries).
- **Organização:** Manter o CSS dentro da tag `<style>` para protótipos simples ou arquivos externos para projetos maiores.

## 🔐 Segurança e Integridade
- **Credenciais:** NUNCA deixar tokens de bots (Discord, Steam API) ou senhas expostas diretamente no código.
- **Ambiente:** Utilizar variáveis de ambiente (`.env`) ou arquivos de configuração externos (como o `secrets.json` mencionado no `BotLevelUp.py`) que devem ser ignorados pelo Git.

## 📂 Organização Sugerida
Se o projeto crescer, recomenda-se a separação em pastas:
- `/web`: Para arquivos `.html` e ativos relacionados.
- `/scripts`: Para utilitários matemáticos de CLI.
- `/bots`: Para implementações de bots do Discord e Steam.
- `/gui`: Para aplicações com interface Tkinter.
