# Importacoes
import cv2
import matplotlib.pyplot as plt

# Exibe imagem em RGB
imagem = cv2.imread("imagens/px-girl.png")
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
plt.imshow(imagem_rgb)

# Exibe imagem em escalas de cinza
imagem_gray = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(imagem_gray, cmap="gray")

# Exibe imagem recortada
imagem_roi = imagem_rgb[200:400, 500:700]
plt.imshow(imagem_roi)

# Exporta imagem recortada
imagem_roi_bgr = cv2.cvtColor(imagem_roi, cv2.COLOR_RGB2BGR)
cv2.imwrite("imagens/imagem_roi.png", imagem_roi_bgr)