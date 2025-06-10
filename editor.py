from PIL import Image, ImageDraw, ImageFont
from temperatura import temperatura

def imageEditor():
  # Abre imagem
  imagem = Image.open('wallpaper.jpg')
  desenho = ImageDraw.Draw(imagem)

  # Dados do tempo
  cidade = "Caxias do Sul"
  texto_titulo = f"{cidade}"
  texto_info = f"Temperatura: {temperatura}°C"

  # Fonte
  try:
      fonte_titulo = ImageFont.truetype("arial.ttf", 80)
      fonte_info = ImageFont.truetype("arial.ttf", 50)
  except IOError:
      fonte_titulo = ImageFont.load_default()
      fonte_info = ImageFont.load_default()

  # Cores
  cor_texto = (255, 255, 255)
  cor_caixa = (0, 0, 0, 160)  # preto com transparência

  # Posição do texto e tamanho da imagem
  largura_img, altura_img = imagem.size

  # Tamanhos do texto
  bbox_titulo = desenho.textbbox((0, 0), texto_titulo, font=fonte_titulo)
  bbox_info = desenho.textbbox((0, 0), texto_info, font=fonte_info)

  largura_box = max(bbox_titulo[2] - bbox_titulo[0], bbox_info[2] - bbox_info[0]) + 80
  altura_box = (bbox_titulo[3] - bbox_titulo[1]) + (bbox_info[3] - bbox_info[1]) + 60

  # Posiciona a caixa no centro da imagem
  pos_x = int((largura_img - largura_box) / 2)
  pos_y = int((altura_img - altura_box) / 2)

  # Cria caixa com fundo translúcido
  caixa = Image.new('RGBA', (largura_box, altura_box), cor_caixa)
  imagem.paste(caixa, (pos_x, pos_y), caixa)

  # Calcula posições para centralizar o texto dentro da caixa
  largura_titulo = bbox_titulo[2] - bbox_titulo[0]
  largura_info = bbox_info[2] - bbox_info[0]

  texto_titulo_x = pos_x + (largura_box - largura_titulo) / 2
  texto_titulo_y = pos_y + 20

  texto_info_x = pos_x + (largura_box - largura_info) / 2
  texto_info_y = texto_titulo_y + (bbox_titulo[3] - bbox_titulo[1]) + 10

  # Escreve o texto na imagem
  desenho = ImageDraw.Draw(imagem)
  desenho.text((texto_titulo_x, texto_titulo_y), texto_titulo, font=fonte_titulo, fill=cor_texto)
  desenho.text((texto_info_x, texto_info_y), texto_info, font=fonte_info, fill=cor_texto)

  # Salva imagem final
  imagem.convert("RGB").save("wallpaper.jpg")

  print("Texto centralizado adicionado com sucesso!")
