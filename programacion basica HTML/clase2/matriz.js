//var menu = ["Productos", "Ventas", "Contacto"];
//document.write(menu[2]);

//Esto es crear un array

function explosion()
{
	alert("BOOM!!");
	document.write("<h1>BOOM! Elegiste un area minada :(</h1>");
}

//Se tiene que invocar a la funcion, hasta este momento la funncion no hace nada"
//Se invoca por medio de su nombre sus parametros "()"
//explosion();

function ganaste()
{
	document.write("Eres un winner!!");
}

//1 = bomba, 0 = no bomba 
var campo = [ [ 1 , 0 , 0 ] , //Array de una sola dimension dividido en tres opciones
			  [ 0 , 1 , 0 ] ,
			  [ 1 , 0 , 1 ] ];

var textos = ["Cesped", "Bomba"];

var x, y;

alert("Estas en un campo minado\n" + 
	"Elije una posicion entre el 0 y el 2 para X y para Y");

x = prompt("¿Posicion en X? (entre 0 y 2)");

y = prompt("¿Posicion en Y? (entre 0 y 2)");


//document.write( textos[posicion] );

if (x <= 2 && y <= 2)
{ 
	var posicion = campo[x][y];
	document.write("Elegiste " + textos[posicion]+ "<br />");

	if(posicion == 1)
	{
		explosion();
	}
	else
	{
		ganaste();
	}

}
else
{
	document.write("Te saliste del campo!");

	explosion();
}
