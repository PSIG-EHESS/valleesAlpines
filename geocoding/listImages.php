<?php

if(isset($_POST["dossiers"])){;

  $dir="Pictures\\".$_POST["dossiers"];//_____________________________________________ Récupération du nom du dossier choisi
  $rii = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));//_______ Itérateur Récursif sur les éléments du dossier

  $files = array(); //________________________________________________________________ Liste qui contiendra les noms et chemins des images

  foreach ($rii as $file) {
      if ($file->isDir()){ continue;}
      $name= (string) $file->getFilename();
      $path= (string) $file->getPathname();
      array_push($files, array('name' => utf8_encode($name), 'path' => utf8_encode($path))); // Ajout du nom et chemin à la liste $files
  }

  echo json_encode($files); // Encodage de la liste finale sous format JSON

}
?>
