import cv2
import time
from ultralytics import YOLO
 

# ================= CORES =================
COR_VERDE = (0, 255, 0)
COR_VERMELHO = (0, 0, 255)
COR_AZUL = (255, 0, 0)
COR_AMARELO = (0, 255, 255)
COR_BRANCO = (255, 255, 255)



# ================= FUNÇÃO TEXTO BONITO =================
def desenhar_texto(img, texto, pos, cor):
    (w, h), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    x, y = pos

    cv2.rectangle(img, (x, y - h - 8), (x + w + 5, y + 5), (0, 0, 0), -1)
    cv2.putText(img, texto, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)



# ================= HUD MELHORADO =================
def desenhar_hud(frame):
    overlay = frame.copy()

    x1, y1 = 10, 10
    x2, y2 = 320, 200

    cv2.rectangle(overlay, (x1, y1), (x2, y2), (20, 20, 20), -1)
    cv2.rectangle(overlay, (x1, y1), (x2, y2), (80, 80, 80), 2)

    for i in range(25):
        cv2.line(overlay, (x1, y1 + i), (x2, y1 + i), (60, 60, 60), 1)

    frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)

    return frame



# ================= CAIXA ESTILIZADA =================
def desenhar_caixa_estilizada(img, x1, y1, x2, y2, cor):
    esp = 2
    tam = 25

    # Cantos
    cv2.line(img, (x1, y1), (x1 + tam, y1), cor, esp)
    cv2.line(img, (x1, y1), (x1, y1 + tam), cor, esp)

    cv2.line(img, (x2, y1), (x2 - tam, y1), cor, esp)
    cv2.line(img, (x2, y1), (x2, y1 + tam), cor, esp)

    cv2.line(img, (x1, y2), (x1 + tam, y2), cor, esp)
    cv2.line(img, (x1, y2), (x1, y2 - tam), cor, esp)

    cv2.line(img, (x2, y2), (x2 - tam, y2), cor, esp)
    cv2.line(img, (x2, y2), (x2, y2 - tam), cor, esp)

    # Centro do objeto
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    cv2.circle(img, (cx, cy), 4, cor, -1)




# ================= YOLO =================
modelo = YOLO("yolov8n.pt")
modelo.fuse()

# ================= CAMERA =================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # <-- WEBCAM EXTERNA
cap.set(3, 640)
cap.set(4, 480)

cv2.namedWindow("Sistema IA", cv2.WINDOW_NORMAL)

pTime = 0
frame_count = 0
resultados = None


# ================= TEMPO =================
tempo_inicio = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao acessar câmera")
        break

    contador_pessoas = 0

    # HUD
    frame = desenhar_hud(frame)

    # Pula frame
    frame_count += 1
    if frame_count % 2 == 0:
        resultados = modelo(frame, conf=0.4, imgsz=480)

    # YOLO
    if resultados is not None:
        for r in resultados:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                classe = int(box.cls[0])
                confianca = float(box.conf[0])

                nome = modelo.names[classe]

                if classe == 0:
                    contador_pessoas += 1

                porcentagem = int(confianca * 100)
                label = f"{nome} {porcentagem}%"

                # CAIXA ESTILIZADA
                desenhar_caixa_estilizada(frame, x1, y1, x2, y2, COR_VERDE)

                # Linha até o texto
                cv2.line(frame, (x1, y1), (x1, y1 - 20), COR_VERDE, 1)

                desenhar_texto(frame, label, (x1, y1 - 25), COR_VERDE)


    # TEMPO         
    if contador_pessoas > 0:
        if tempo_inicio is None:
            tempo_inicio = time.time()

        tempo_atual = int(time.time() - tempo_inicio)

        desenhar_texto(frame, f"Tempo: {tempo_atual}s", (20, 150), COR_AMARELO)

        if int(time.time() * 2) % 2 == 0:
            cv2.putText(frame, "ALERTA: Pessoa detectada!",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        COR_VERMELHO,
                        2)
            
    else:
        tempo_inicio = None


    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime

    desenhar_texto(frame, f'FPS: {int(fps)}', (20, 70), COR_AZUL)

    # CONTADOR
    desenhar_texto(frame, f'Pessoas: {contador_pessoas}', (20, 110), COR_AMARELO)
 

    # TÍTULO
    cv2.putText(frame, "Sistema de Monitoramento IA",
                (140, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                COR_BRANCO,
                2)

    cv2.imshow("Sistema IA", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

