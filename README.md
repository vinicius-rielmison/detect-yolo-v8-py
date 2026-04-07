# 🧠 Sistema de Monitoramento com IA (YOLOv8 + OpenCV)

Este projeto é um sistema de visão computacional em tempo real desenvolvido em Python, capaz de detectar pessoas utilizando inteligência artificial com o modelo YOLOv8. Ele exibe informações visuais avançadas (HUD), contador de pessoas, FPS, tempo de permanência e alertas dinâmicos.

---

## 🚀 Funcionalidades

* 🔍 Detecção de objetos em tempo real com YOLOv8
* 👤 Contagem automática de pessoas
* ⏱️ Monitoramento de tempo de permanência na câmera
* ⚠️ Sistema de alerta visual quando há pessoas detectadas
* 🎨 Interface estilizada com HUD (Heads-Up Display)
* 📊 Exibição de FPS (Frames por segundo)
* 📦 Bounding boxes estilizadas com destaque visual

---

## 🖥️ Tecnologias Utilizadas

* Python 3.x
* OpenCV
* Ultralytics YOLOv8

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as dependências:

```bash
pip install opencv-python ultralytics
```

---

## ▶️ Como Executar

Execute o script principal:

```bash
python main.py
```

Pressione a tecla **Q** para encerrar o sistema.

---

## 📷 Como Funciona

O sistema utiliza a webcam para capturar vídeo em tempo real e aplica o modelo YOLOv8 para detectar objetos. Quando uma pessoa é identificada:

* Um contador é incrementado
* Um alerta visual é exibido
* O tempo de permanência começa a ser contado

---

## 🧩 Estrutura do Código

* `desenhar_texto()` → Exibe textos com fundo estilizado
* `desenhar_hud()` → Cria o painel visual (HUD)
* `desenhar_caixa_estilizada()` → Desenha bounding boxes customizadas
* Loop principal → Captura, processa e exibe os frames

---

## ⚙️ Configurações

Você pode ajustar:

* 🔧 Resolução da câmera:

```python
cap.set(3, 640)
cap.set(4, 480)
```

* 🎯 Confiança da detecção:

```python
modelo(frame, conf=0.4)
```

---

## 📌 Melhorias Futuras

* 📁 Gravação de vídeo
* 🔔 Alertas sonoros
* 🌐 Integração com sistemas web
* 🧠 Treinamento de modelo personalizado
* 📊 Dashboard com estatísticas

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

---

## 🤝 Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues ou pull requests.

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius Rielmison Rocha de Sousa**
GitHub: https://github.com/vinicius-rielmison

---

## ⭐ Dê uma estrela!

Se este projeto te ajudou, considere dar uma ⭐ no repositório!

---
