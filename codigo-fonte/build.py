import base64,re
def uri(f): return 'data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode()
t=open('template.html',encoding='utf-8').read()
t=(t.replace('__MARK__',uri('../imagens/mark.webp')).replace('__CAMERA__',uri('../imagens/camera.webp'))
     .replace('__CIRCLE__',uri('../imagens/circle.webp')).replace('__PORTRAIT__',uri('../imagens/portrait.webp')))
# versão para o artefato (o publicador adiciona o esqueleto da página)
open('rossini-artefato.html','w',encoding='utf-8').write(t)
# versão independente (index.html): inclui doctype, idioma e viewport de celular
i=t.index('<svg width="0"')
head,body=t[:i],t[i:]
head=head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
standalone=('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  +head+'<style>:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n')
open('../index.html','w',encoding='utf-8').write(standalone)
print(round(len(t.encode())/1024,1),'KB | placeholders:',re.findall(r'__[A-Z]+__',t))
