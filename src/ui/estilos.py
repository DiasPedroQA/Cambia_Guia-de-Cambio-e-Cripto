# src/ui/estilos.py

"""Estilos CSS personalizados para a interface."""

import streamlit as st


def aplicar_estilos() -> None:
    """Aplica estilos CSS personalizados na aplicação."""
    st.markdown(body="""
    <style>
        /* Cores principais */
        :root {
            --cor-primaria: #6C5CE7;
            --cor-secundaria: #00B894;
            --cor-alerta: #FDCB6E;
            --cor-perigo: #E17055;
        }
        
        /* Título principal */
        .main-header {
            background: linear-gradient(90deg, #6C5CE7, #00B894);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }
        
        /* Cards de cotação */
        .cotacao-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
            border-radius: 15px;
            color: white;
            margin: 0.5rem 0;
        }
        
        /* Métricas personalizadas */
        [data-testid="stMetricValue"] {
            font-size: 1.4rem;
            font-weight: bold;
        }
        
        /* Alertas animados */
        .stWarning {
            animation: pulse 2s infinite;
            border-left: 5px solid #FDCB6E;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }
        
        /* Chat melhorado */
        [data-testid="stChatMessage"] {
            border-radius: 15px;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #2d3436 0%, #636e72 100%);
        }
        
        /* Scrollbar personalizada */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #6C5CE7;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
