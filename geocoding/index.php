<?php
$dirs = glob('Pictures\*' , GLOB_ONLYDIR); // Récupération de tous les dossiers contenus dans le répertoire "Pictures"
 ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">

    <title>Géolocalisation de Photos</title>

    <link rel="stylesheet" href="https://npmcdn.com/leaflet@1.2.0/dist/leaflet.css" />
    <script src="https://npmcdn.com/leaflet@1.2.0/dist/leaflet.js"></script>
    <script src="https://npmcdn.com/leaflet.path.drag/src/Path.Drag.js"></script>

    <script src="ressources/Leaflet.Editable.js"></script>

    <script src="ressources/jquery-3.2.1.min.js" charset="utf-8"></script>

    <link rel="stylesheet" href="ressources/geolocalisation.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  </head>

  <body>

    <h1 class="display-4 text-secondary" id="title"> Géolocalisation de photos </h1>
    <!-- ______________________ Formulaire de sélection de dossier de photos souhaité (peut contenir des sous-dossiers) ___________________________ -->
    <form id="form_directory" class="col-md-10">
      <div class="input-group">
        <div class="input-group-prepend col-md-4 bg-light text-center">
          <label class="input-group-text" for="inputGroupSelect"> <span class="align-middle"> Choisir le dossier de photos</span></label>
        </div>
         <?php
         if (sizeof($dirs)==0) { //____________ s'il n'y a aucun dossier dans le répertoire
           echo "<p>Veuillez mettre un dossier de photos dans le dossier Pictures</p>";
         } else { //___________________________ sinon : Affichage des noms de dossiers disponibles dans une liste déroulante
           echo "<select name='dossiers' class='custom-select col-md-6' id='inputGroupSelect'>";
           foreach ($dirs as $dir) {
             $nomDir= utf8_encode(basename($dir));
             echo "<option value='$nomDir'>$nomDir</option>";
           }
           echo "</select>";
           echo "<input id='choose' type='submit' name='choose' value='Valider' class='btn btn-secondary col-md-2'>";// Boutton de valisation
         } ?>
         </div>
    </form>
    <!-- ____________________________________________ Bloc d'affichage de la carte ________________________________________________________________ -->
    <div class="col-md-10" id="map_container">
      <div id="mapid">
      </div>
    </div>
    <!-- ______________________________________________ Bouttons de téléchargement ________________________________________________________________ -->
    <div class="form-group">
      <button type="button" id="download_sucess" class="btn btn-primary" disabled>Télecharger la table des images géolocalisées</button>
      <button type="button" id="download_failed" class="btn btn-primary" disabled>Télecharger la table des images non géolocalisées</button>
    </div>
    <!-- ___________________________________________ Bas de page __________________________________________________________________________________ -->
    <footer class="container col-md-12 row">
       <div class="col-md-4">
               <p class="blockquote-footer">Projet Recherche</p>
       </div>
       <div class="col-md-8">
               <p class="text-right blockquote-footer"> 2017-2018 École Nationale de Sciences Géographiques - École des Hautes Études en Sciences Sociales</p>
       </div>
    </footer>
    <!-- ___________________________________________________________________________________________________________________________________________ -->
    <script src="geolocalisation.js" charset="utf-8"></script>
  </body>
</html>
