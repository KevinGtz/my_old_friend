//*FORMA CORRECTA DE ESCRIBIR JS*

//Creamos una funcion llamada Pokemon con tres parametros 
//n, vy a son los parametros que posee la funcion pokemon 
function Pokemon(n,v,a)
{
	//referenciamos las variables con los parametros de la funcion
	this.nombre = n;
	this.vida = v;
	this.ataque = a;
	this.imagen = function()
	{ 
		var img = new Image();
		var div = document.getElementById('imagen');

		img.onload = function() {
			div.appenChild(img);
		};
		img.src = 'images/charmander.jpg';
}
	//se crea un metodo 
	this.grito = "Pika";
	this.gritar = function ()
	{
		alert(this.grito);
	}
}

function inicio()
{//Se crea un nuevo Pokemon llamado charmander y con sus respectivos atributos
	var charmander = new Pokemon("Charmander", 150, 60);
	charmander.vida = charmander.vida + 34;
	charmander.grito = "chaaaaaaar";
	charmander.gritar();
	charmander.imagen;


	nombrePokemon.innerText = charmander.nombre;
	datosPokemon.innerText = charmander.vida;
	datosPokemon_1.innerText = charmander.ataque;
	datosPokemon_2.innerText = charmander.grito;
}


//function inicio()
//{//Se crea un nuevo Pokemon llamado rattata y con sus respectivos atributos
	//alert("esto es despues del inicio");
	//var rattata = new Pokemon("Rattata", 40, 2);
	//rattata.vida = rattata.vida - 23;

	//nombrePokemon.innerText = rattata.nombre;
	//datosPokemon.innerText = rattata.vida, rattata.ataque
//}

//alert("esto es antes del inicio");


/*
function Pokemon(nombrePoke, vidaPoke, ataquePoke)
{
	var estructuraPokemon =
	{
		nombre: nombrePoke,
		vida: vidaPoke,
		ataque: ataquePoke,
		//Creamos una estructura de datos dentro de una estructura de datos
		//Estamos indicando que todos los pokemon creados van a ser de tipo tierra y debiles al fuego
		datos: {tipo : "Tierra", debilidad: "Fuego"}
	};
	return estructuraPokemon
}

var pikachu = Pokemon("Pikachu", 100, 55);
var bulbasaur = Pokemon("bulbasaur", 90, 50);

document.write(pikachu.nombre + "<br />" + pikachu.vida + "<br />" );
document.write(bulbasaur.nombre + "<br />"  + bulbasaur.vida + "<br />" );
document.write(bulbasaur.datos.debilidad);

console.log(bulbasaur);


function Pokemon() // Se crea una funcion llamada pokemon
{
	//Se crea una estructura
	var estructuraPokemon = 
	{
		nombre: "Pikachu",
		vida : 100,
		ataque:55
	};
	//Retorna la estructura sin que sea una funcion
	return estructuraPokemon;
}

var pikachu = Pokemon(); //para invocar funciones se necesita su nombre y los parametro a invocar entre un parentesis y al final un ;
var bulbasaur = Pokemon();
bulbasaur.nombre = "Bulbasaur";
bulbasaur.vida = 90;
bulbasaur.ataque = 50;

document.write(bulbasaur.nombre, bulbasaur.vida  );

//programa distinto*
se crea un objeto llamado pokemon 
var Pokemon = 
{
	nombre: "Pikachu",
	tipo: "Electrico",
	vida: 100,
	ataque: 22,

}; // al crear un objeto es el unico caso donde un bloque lleva ";"

var Pikachu = */