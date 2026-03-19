#!/usr/bin/node

// récupérer tous les arguments passés après le script
const args = process.argv.slice(2); 

if (args.length === 0) {
  console.log('No argument'); // aucun argument
} else if (args.length === 1) {
  console.log('Argument found'); // un seul argument
} else {
  console.log('Arguments found'); // plusieurs arguments
}