//Exemple d'un code JavaScript

<script>
        // Charger le dictionnaire français de Typo.js
        var dictionary = new Typo("fr_FR");

        // Sélectionner l'élément avec la classe "autocomplete"
        var input = document.querySelector(".autocomplete");

        // Variable pour stocker le timer
        var inputTimer;

        // Écouter l'événement d'entrée pour vérifier l'orthographe
        input.addEventListener("input", function() {
            clearTimeout(inputTimer);

            // Utiliser setTimeout pour retarder l'exécution du code
            inputTimer = setTimeout(function() {
                var searchTerm = input.value;
                var suggestions = dictionary.suggest(searchTerm).slice(0, 5); // Limite à 5 suggestions

                // Afficher les suggestions sous la barre de recherche
                var suggestionContainer = document.getElementById("suggestion-container");
                suggestionContainer.innerHTML = "";
                suggestions.forEach(function(suggestion) {
                    var suggestionElement = document.createElement("div");
                    suggestionElement.innerHTML = "Vous voulez dire : <span style='color: blue;'>" + suggestion + "</span>";
                    suggestionElement.addEventListener("click", function() {
                        input.value = suggestion;
                        suggestionContainer.innerHTML = ""; // Effacer les suggestions après la sélection
                    });
                    suggestionContainer.appendChild(suggestionElement);
                });
            }, 200); // Délai de 200 ms (ajustez selon vos besoins)
        });
  </script>