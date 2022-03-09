# escribe-html.py

f = open('holamundo.html','w')

mensaje = '''<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>Grupo Leon</title>
  </head>
  
    <h1>Confirmación de pedido</h1>
	<h3>“PROCESADORA  COMERCIALIZADORA DE NUECES  Y  PIÑONES  LEON HERMANOS  S.A de C.V”</h3>
	
	<body>
	<table>
    <tr>
        <td>	</td>
        <td>Cliente:</td>
        <td>Juan Rodriguez</td>
		<td>		</td>
        <td>Fecha de entrega</td>		
        <td>01-03-22</td>
		<td><img src="logo.png" alt="logo"></td>
        
    </tr>
    <tr>
        <td>	</td>
        <td>Cantidad</td>
        <td>Unidad</td>
        <td>Producto</td>
        <td>Costo unitario</td>
        <td>Sub. Total</td>
    </tr>

    <tr>
		<td>	</td>
        <td>10</td>
        <td>kg</td>
        <td>Mangomitas</td>
        <td>110</td>
        <td>1100</td>
        
    </tr>
</table>

  </body>
</html>'''






f.write(mensaje)
f.close()
