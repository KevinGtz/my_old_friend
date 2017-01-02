//Document Object Model
//Los tres principales objetos de JS
// --Navigator --Window --Document
//Objeto
// Variables
// Funciones

//document.write("hola mama");
// var pi = 3.141592654;
//pi = Math.floor(pi);
//pi = Math.ceil(pi);
//document.write(pi);

document.write("holi a todos");
var maxima;
maxima = Math.max(5, 23 ,4, 5, 12, 23, 23);
document.write(maxima);

function mostrar(pos) 
{
	document.write(pos.coords.latitude + "," + pos.coords.longitude);
}
 	navigator.geolocation.getCurrentPosition(mostrar);