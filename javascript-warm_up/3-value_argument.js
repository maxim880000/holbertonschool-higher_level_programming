#!/usr/bin/node

// récupérer le premier argument (après node et le script)
const arg = process.argv[2]; 

if (arg) {
  console.log(arg); // affiche l'argument si présent
} else {
  console.log('No argument'); // aucun argument
}