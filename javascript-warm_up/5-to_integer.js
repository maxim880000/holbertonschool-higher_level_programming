#!/usr/bin/node

// récupérer le premier argument
const arg = process.argv[2]; 

// convertir en entier
const num = parseInt(arg); 

// vérifier si c'est un nombre
if (isNaN(num)) {
  console.log('Not a number'); // pas convertible en entier
} else {
  console.log('My number: ' + num); // afficher l'entier
}
