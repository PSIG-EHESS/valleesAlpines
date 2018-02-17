
/*------------------------------------------Création de la map ---------------------------------------------------------------------------------------*/
// Création d'une carte grâce à la librairie leaflet www.http://leafletjs.com/reference-1.3.0.html
var map = L.map('mapid', {editable: true}).setView([46.225453, 11.173096], 6);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'   // fond de carte OSM
}).addTo(map);

// liste des points représentant l'emprise géographique (Alpes)
 var polyPoints= [ [ 43.555313449518188, 7.451565963486024 ], [ 43.85825110558995, 5.068112527010708 ], [ 46.239036983684905,  5.409346835695028 ],
  [ 47.648231026946412, 7.111072615418121 ], [ 48.462280532922271, 17.194914077429072 ], [ 45.72147389821987, 16.900256372370308 ],
  [ 45.602527009820022, 13.756149228215332 ], [ 46.155344584475728, 13.18794751968275 ], [ 45.390184486323889, 11.007069707401246 ],
  [ 45.832317970265365, 8.722093481841858 ], [ 45.414153997142208, 7.75203318620867 ], [ 44.962550698603124, 7.433158696905728 ],
  [ 44.330784291865363, 7.542444281316445 ], [ 44.344860006573647,  9.174754266077134 ], [ 43.555313449518188, 7.451565963486024 ]];

var emprise =L.polygon(polyPoints).addTo(map);
emprise.enableEdit();
/*----------------------------------------------------------------------------------------------------------------------------------------------------*/

/*-------------------------------------------MAIN-----------------------------------------------------------------------------------------------------*/

// Initialisation des variables globales
var success_list=[], failed_list=[], total_pictures, directory;
//success_list(liste les images géolocalisées); failed_list(liste des images non géolocalisées);
//total_pictures(nombre total de photos); directory(dossier de photos choisies)

 //Récupération du formulaire de sélection du dossier et des bouttons de téléchargements de fichiers CSV
var form_directory= document.getElementById('form_directory');
var downloadButton_sucess= document.getElementById('download_sucess');
var downloadButton_failed= document.getElementById('download_failed');

//Associer des écouteurs d'évenements au deux bouttons de télécharchement
header_sucess="Nom;Lieu;Latitude;Longitude;Chemin\n";
downloadButton_sucess.addEventListener("click", function f(e){ write_CSV(success_list, header_sucess, ""); }); // CSV de la liste success_list
header_failed="Nom;Chemin\n";
downloadButton_failed.addEventListener("click", function f(e){ write_CSV(failed_list, header_failed, "_failed"); }); // CSV de la liste failed_list


//-----------------------Lancer le géocodage des noms de photos contenues dans le dossier choisi------------------------------------------------------
form_directory.addEventListener("submit", function f(e){
  e.preventDefault();
  //Désactivation des deux bouttons de téléchargements
  downloadButton_sucess.disabled=true;
  downloadButton_failed.disabled=true;
  //Réinitialisation des deux listes success_listet failed_list
  while (success_list.length > 0) {
    success_list.pop();
  }
  while (failed_list.length > 0) {
    failed_list.pop();
  }
  polyPoints=emprise._latlngs;
  //Définition d'une requête AJAX pour récupérer les photos contenues dans le dossier choisi (sous-dossiers inclus)
  var ajax = new XMLHttpRequest();
  ajax.open('POST', "listImages.php", true);
  ajax.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

  ajax.addEventListener('readystatechange',  function(e) {
      if(ajax.readyState == 4 && ajax.status == 200) {
           var resultat=JSON.parse(ajax.responseText); //____________ resultat: liste des images {nom de l'image, chemin relatif}
           total_pictures=resultat.length; //________________________ affectation du nombre total de photos
           if (total_pictures==0) { alert("Dossier Vide !"); }
           for (var i = 0; i < total_pictures; i++) {
             let image_name= resultat[i].name.split(".jpg")[0];
             let path= resultat[i].path;
             let img=[image_name,path];
             // Géocodage asynchrone de chaque image en commançant par l'API OpenStreetMap; callback_OSM est la fonction qui traîtera le resultat
             Geocode(img, API_OSM, callback_OSM);
           }
      }
  });
  let dirs = form_directory.elements["dossiers"]; directory=dirs.options[dirs.selectedIndex].value; //nom du répertoire choisi
  let data = "dossiers="+directory;
  ajax.send(data);

});
/*----------------------------------------------------------------------------------------------------------------------------------------------------*/


 /*------------------------------------------- Définition des fonctions ------------------------------------------------------------------------------*/

 //----------------------------- Fonction Géocodage qui envoie une requête HTTP AJAX au seveur de l'api ----------------------------------------------
 function Geocode(img, api, callback){
    // Définition de l'url de la requête en fonction de l'API utilisé
    var url=api.url+Clean_Name(img[0]); //Géocodage par nom de l'image, Clean_Name() permet d'extraire uniquement le nom de la localité
    if (api==API_OSM) {
      url+="?format=json";}

    $.ajax({
      url : url,
      type : 'GET',
      async : true, //_________________________________ requêtes HTTP asynchrones
      retryCount: 0,//_________________________________ compteur pour le nombre de tentatives
      retryLimit: 3,//_________________________________ Limite de tentatives
      dataType: "json",
      // En cas de succès de la requête HTTP :
      success : function(result) {
        // lecture du resultat selon l'API
        let lat= api.Read_JSON(result)[0];//___________ Latitude
        let lng= api.Read_JSON(result)[1];//___________ Longitude
        let f_adress= api.Read_JSON(result)[2];//______ Adresse ou nom fourni par l'API
        let coord= [lat, lng, f_adress];
        //Envoi du résultat à la fonction callback ( callback_OSM ou callback_photon selon les paramètres)
        callback(img, coord);
      },
      // En cas d'erreur dans l'envoi de la requête HTTP :
      error:  function (req) {
        if (req.status == 503 || req.status == 429 || req.status == 0) { // Serveur de l'API qui répond pas

          this.retryCount++; //_______________________________ Incrémentation du nombre de tentatives

          if (this.retryCount <= this.retryLimit) { //________ Si la limite de tentatives n'est pas dépassée
             setTimeout(() => { $.ajax(this) }); //___________ Renvoi de la requête HTTP
          }
          else { add_to_failedList(img);} //___________________ Si la limite est dépassée appel de la fonction add_to_failedList()
        }

        else { add_to_failedList(img);} //_____________________________// Autres sources d'erreur: appel de la fonction add_to_failedList()
      }
     });
 };

//---------------------------------- Fonctions Callback relatives à chaque API ------------------------------------------------------------------------

 function callback_OSM(img, coord){
   if (coord[0]==0 || coord[1]==0) {//______________ Si l'une des coordonnées correspond à 0 (signifiant aucun résultat par géocodage OSM)
     Geocode(img, API_PHOTON, callback_photon);//___ Nouvelle tentative de géocodage par l'API Photon
   }
   else {
     add_to_successList(img, coord); //_____________________ Sinon: Appel de la fonction add_to_successList()
   }
 };

function callback_photon(img, coord){
  if (coord[0]==0 || coord[1]==0) { //______________ Si l'une des coordonnées correspond à 0 (aucun résultat par géocodage Photon également)
    add_to_failedList(img); //______________________ Appel de la fonction add_to_failedList()
  }
  else {
    add_to_successList(img, coord); //_____________________ Sinon: Appel de la fonction add_to_successList()
  }
};

//---------------------------------- Fonctions add_to_successList et add_to_failedList ----------------------------------------------------------------

function add_to_successList(img, coord){
  // Nouvelle ligne: {"nom de l'image", "adresse récupérée par l'API", "Latitude", "Longitude", "chemin relatif"}
  let row=[img[0],coord[2],coord[0],coord[1],img[1]];
  success_list.push(row);   // Ajout de la ligne à la liste success_list
  check_geocode_complete(); // Vérifier si toutes les images ont été traîtées
}

function add_to_failedList(img){
  failed_list.push(img);   // Ajout d'une ligne: {"nom de l'image", "chemin relatif"} à la liste failed_list
  check_geocode_complete();// Vérifier si toutes les images ont été traîtées
}

//----------------------------------------- Fonctions check_geocode_complete --------------------------------------------------------------------------
function  check_geocode_complete(){
  // Condition: La somme des images géocodées et non géocodées est égale au nombre total des images
  if(success_list.length+failed_list.length==total_pictures){
    // Activation des bouttons de téléchargement des deux fichiers CSV correspondant à la liste des images géocodées ou celle des images non géocodées
    downloadButton_sucess.disabled= false;
    downloadButton_failed.disabled= false;
  }
}

 //-----------------------------------Définition des deux API et méthodes de lecture des résultats------------------------------------------------------
// https://wiki.openstreetmap.org/wiki/Nominatim
 const API_OSM={
   url:"http://nominatim.openstreetmap.org/search/",
   // Méthode pour la lecture du JSON renvoyé selon la structure définie par l'API Nominatim OSM et choix du résultat
   Read_JSON: function(obj){
     if (obj.length!=0) {
       for (var i = 0; i < obj.length; i++) { // ________ Parcourir la liste des points renvoyée
         let lat= obj[i].lat;
         let lng= obj[i].lon;
         let f_adress= obj[i].display_name;
         if (isInsidePolygon(lat,lng,polyPoints)) {
           return [lat,lng,f_adress]; // ________________ Si le point est dans l'emprise géographique définie
         }
       }
     }
     return [0,0,"Aucun Résultat sur OSM API"]; // ______ Si aucun point ne se situe dans l'emprise
   }
 }
 //http://photon.komoot.de/
 const API_PHOTON={
   url:"https://photon.komoot.de/api/?q=",
   // Méthode pour la lecture du JSON renvoyé selon la structure définie par l'API PHOTON et choix du résultat
   Read_JSON: function(obj){
     if (obj.features.length!=0) {
       for (var i = 0; i < obj.features.length; i++) {
         let lat= obj.features[i].geometry.coordinates[1];
         let lng= obj.features[i].geometry.coordinates[0];
         let f_adress= obj.features[i].properties.name;
         if (isInsidePolygon(lat,lng,polyPoints)) {
           return [lat,lng,f_adress];
         }
       }
     }
     return [0,0,"Aucun Résultat sur PHOTON API"];
   }
 }

//-----------------------------------------Fonction qui vérifie si Point est dans Polygone-------------------------------------------------------------
function isInsidePolygon(lat, lng, polyPoints) {
    let inside = false;
    for (var i = 0, j = polyPoints[0].length - 1; i < polyPoints[0].length; j = i++) {
        let lati = polyPoints[0][i].lat, lngi = polyPoints[0][i].lng;
        let latj = polyPoints[0][j].lat, lngj = polyPoints[0][j].lng;
        let intersect = ((lngi > lng) != (lngj > lng))
            && (lat < (latj - lati) * (lng - lngi) / (lngj - lngi) + lati);
        if (intersect) inside = !inside;
    }
    return inside;
};

//-----------------------------------Fonction qui récupère le nom de la localité sans numéros et lettres-----------------------------------------------
function Clean_Name(nom){
  let regex1= /.+\s([0-9])/;
  let regex2= /.+\s([a-z])$/;
  let regex3= /.+\s(annexe)/;
  let regex4= /.+\s(\(au-dessus\))/
  let regex5=/(Au-dessus)\s(de|du)\s.+/

  if (regex5.exec(nom)!=null) {
    nom= nom.split(/(Au-dessus)\s(de|du)\s/)[3];
  }
  if (regex1.exec(nom)!=null) {
    nom= nom.split(/\s([0-9])/)[0];
  }
  if (regex2.exec(nom)!=null) {
    nom= nom.split(/\s([a-z])$/)[0];
  }
  if (regex3.exec(nom)!=null) {
    nom= nom.split(/\s(annexe)/)[0];
  }
  if (regex4.exec(nom)!=null) {
    nom= nom.split(/\s(\(au-dessus\))/)[0];
  }
  return nom;
}

//--------------------------------Fonction qui permet d'écrire un fichier CSV à partir d'une liste----------------------------------------------------
function write_CSV(list, header, name){
  var csvContent = header;
  list.forEach(function(infoArray, index) {
    dataString = infoArray.join(';');
    csvContent += index < list.length ? dataString + '\n' : dataString;
  });
  var download = function(content, fileName, mimeType) {
    var a = document.createElement('a');
    mimeType = mimeType || 'application/octet-stream';
    if (navigator.msSaveBlob) { // IE10
      navigator.msSaveBlob(new Blob([content], {
        type: mimeType
      }), fileName);
    } else if (URL && 'download' in a) { //html5 A[download]
      a.href = URL.createObjectURL(new Blob([content], {
        type: mimeType
      }));
      a.setAttribute('download', fileName);
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    } else {
      location.href = 'data:application/octet-stream,' + encodeURIComponent(content);
    }
  }
  download(csvContent, directory+name+'.csv', 'text/csv;encoding:utf-8');
}
/*----------------------------------------------------------------------------------------------------------------------------------------------------*/
