// On sélectionne le <div id="red_header"> sur lequel l'utilisateur va cliquer
const redButton = document.querySelector('#red_header');

// On écoute l'événement "click" sur cet élément
// Quand l'utilisateur clique, la fonction s'exécute
redButton.addEventListener('click', function() {

  // On sélectionne le <header> et on change sa couleur en rouge
  document.querySelector('header').style.color = '#FF0000';

});