# 📊 Análise de Séries Temporais

Projeto de análise e previsão de séries temporais com foco em previsão de vendas para e-commerce usando modelos avançados de machine learning.

## 📋 Descrição

Este projeto implementa análises de séries temporais e modelos de previsão, incluindo:

- **Previsão de Vendas**: Modelo Holt-Winters para prever vendas diárias considerando tendência e sazonalidade
- **Visão Computacional**: Análises e aplicações de computer vision
- **Análise Exploratória**: Exploração de padrões, tendências e comportamentos sazonais

## 🎯 Objetivo

Desenvolver modelos preditivos robustos para prever vendas futuras de uma plataforma de e-commerce, levando em consideração:
- Tendência de crescimento ao longo do tempo
- Padrões sazonais (variações semanais, picos nos finais de semana)
- Ruído e variabilidade natural nos dados

## 📁 Estrutura do Projeto

```
series temporais/
├── src/
│   ├── vidente_vendas.py          # Modelo de previsão de vendas com Holt-Winters
│   └── visao_computacional.ipynb  # Análises de visão computacional
├── requirements.txt               # Dependências do projeto
├── .gitignore                     # Arquivos ignorados pelo Git
├── .venv/                         # Ambiente virtual Python
└── README.md                      # Este arquivo
```

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone ou acesse o projeto**:
```bash
cd "series temporais"
```

2. **Crie um ambiente virtual** (recomendado):
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**:
   - **Windows**:
   ```bash
   .venv\Scripts\activate
   ```
   - **Linux/macOS**:
   ```bash
   source .venv/bin/activate
   ```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## 💻 Como Usar

### Executar Previsão de Vendas

```bash
python src/vidente_vendas.py
```

**Saída esperada**:
```
📅 Histórico de dados: 01/01/2025 até 31/12/2025
💰 Média de vendas diárias: R$ 1800.50

📈 --- PREVISÃO DE VENDAS PARA A PRÓXIMA SEMANA ---
🗓️  01/01/2026 (segunda): R$ 3050.25
🗓️  02/01/2026 (terça): R$ 3120.75
...
```

### Análise de Visão Computacional

Abra o notebook Jupyter:
```bash
jupyter notebook src/visao_computacional.ipynb
```

## 📦 Dependências Principais

- **pandas** (2.1.4): Manipulação e análise de dados
- **numpy** (1.26.4): Computação numérica
- **scipy** (1.11.4): Ferramentas científicas
- **scikit-learn** (1.4.2): Machine learning
- **statsmodels** (0.15.0): Modelos estatísticos e séries temporais
- **matplotlib** (3.7.5): Visualização de dados
- **plotly** (6.9.0): Gráficos interativos
- **lightgbm** (4.7.0): Gradient boosting
- **Flask** (3.1.3): Framework web
- **Jupyter** (5.9.1): Notebooks interativos

## 🔧 Tecnologias Utilizadas

### Modelos de Séries Temporais
- **Holt-Winters (ExponentialSmoothing)**: Modelo com tendência e sazonalidade
- Suporte para componentes aditivos e multiplicativos

### Visualização
- Matplotlib para gráficos estáticos
- Plotly para visualizações interativas

### Análise de Dados
- Pandas para manipulação e análise
- NumPy para computação numérica
- SciPy para análises estatísticas

### ML e Deep Learning
- Scikit-learn para modelos tradicionais
- LightGBM para gradient boosting
- Imbalanced-learn para tratamento de dados desbalanceados

## 📊 Metodologia

### Modelo Holt-Winters Utilizado

O modelo implementa:

1. **Componente de Tendência** (`trend='add'`): Captura o crescimento/decrescimento ao longo do tempo
2. **Componente Sazonal** (`seasonal='add'`): Identifica padrões que se repetem a cada 7 dias (ciclo semanal)
3. **Ruído**: Variabilidade natural nos dados

### Dataset de Exemplo

- **Período**: 1 ano (365 dias) - 01/01/2025 a 31/12/2025
- **Tendência**: Crescimento linear de R$ 1.000 a R$ 3.000
- **Sazonalidade**: Padrão semanal com picos nos finais de semana
- **Ruído**: Distribuição normal com σ = 100

## 📈 Resultados Esperados

- Previsões precisas para os próximos 7 dias
- Captura de padrões sazonais semanais
- Identificação de tendências de crescimento
- Métricas de avaliação (MAE, RMSE, etc.)

## 🔍 Extensões Futuras

- [ ] Implementar ARIMA/SARIMA para validação comparativa
- [ ] Integrar Prophet (Facebook) para previsões mais robustas
- [ ] Adicionar análise de intervalo de confiança
- [ ] Criar API REST para servir previsões em tempo real
- [ ] Dashboard interativo com Dash/Streamlit
- [ ] Backtesting e validação de modelos
- [ ] Análise de séries temporais multivariadas

## 🤝 Contribuindo

Para contribuir com melhorias:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está disponível sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões sobre este projeto, abra uma issue ou entre em contato.

## 🎓 Referências

- [Statsmodels Documentação](https://www.statsmodels.org/)
- [Pandas Documentação](https://pandas.pydata.org/)
- [Scikit-learn Documentação](https://scikit-learn.org/)
- [Guia de Séries Temporais](https://otexts.com/fpp2/)

---

**Última atualização**: Setembro de 2026
**Status**: ✅ Ativo e em desenvolvimento
