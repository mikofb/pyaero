"""
	Here is the loader file.
	When PyAero starts, this file set up:
		→ the differents words used in the such popup sentences and the PyAero UI words
		→ the pictures used
	All these changements are done by regarding the settings variables in Settings/settings.py file first.
	And finally the values will be used in the ./PyAero.py file
"""

import os
import sys


IMAGES = ["pyaero_logo.ico","pyaero_screensplash.png","prev.png","next.png","refresh.png","desktop.png","document_folder.png","pictures_folder.png","music_folder.png","video_folder.png",
"downloads_folder.png","disk.png","settings.png","about.png","folder.png","archive_folder.png","music_file.png",
"video_file.png","pdf_file.png","other_file.png","picture.png","link_file.png","python_file.png","php_file.png","powerpoint_file.png","html_file.png",
"java_file.png","exe_file.png","excel_file.png","css_file.png","cpp_file.png","c_file.png","access_file.png","word_file.png","text_file.png","crt.png",
"disk_file.png","dll_file.png","header_file.png","htm_file.png","log_file.png","perl_file.png","rpm_file.png","rtf_file.png","sql_file.png","xml_file.png",
"deb_file.png"]


MAIN_WORDS_FR = ['Filtre vide','Veuillez renseigner le filtre de recherche.\nPour rechercher les fichiers n\'ayant pas\n d\'extension,\
 précédez le champ de saisie de \'/\'.','Elément(s)','Dossier(s)','Fichier(s)','Résultats','Aucune correspondance trouvée.']
MAIN_WORDS_EN = ['Empty pattern','Please enter a pattern for research.\nIf you are looking for file(s) without extension,\
 enter: \'/\' first.','Element(s)','Folder(s)','File(s)','Results','No matches found.']

CONTEXT_MENU_FR = ['Ouvrir','Compresser','Décompresser','Copier','Couper','Coller','Supprimer','Renommer','Nouveau','Propriétés']
CONTEXT_MENU_EN = ['Open','Compress','Uncompress','Copy','Cut','Paste','Delete','Rename','New','Properties']

LEFT_SIDE_WORDS_FR = ['Ordinateur','Bureau','Documents','Images','Musique','Vidéos','Téléchargements','Disques et périphériques',
'Disque Local','','Paramètres', 'A Propos']
LEFT_SIDE_WORDS_EN = ['Computer','Desktop','Documents','Pictures','Music','Videos','Downloads','Disks and devices',
'Local Disk','','Settings', 'About']

OTHERS_WORDS_FR = ['Rechercher dans','Taille','Recherche en cours...']
OTHERS_WORDS_EN = ['Search in', 'Size','Search in progress...']

FILE_NAME_FR = ['Fichier','Fichier sans extension','Fichier PDF','Fichier Vidéo','Dossier d\'archive','Fichier Audio','Fichier Image','Racourcis','Fichier source Python','Fichier script PHP',
'Document Microsoft Powerpoint','Fichier HTML','Fichier source JAVA','Application de Bureau','Document Microsoft Excel','Feuille de style','Fichier source C++',
'Fichier source C','Document Microsoft Word','Fichier Texte','Certificat de sécurité','Fichier Image','Extensiond d\'application','Fichier Header','Fichier HTM',
'Fichier journal','Fichier source PERL','Paquet','Fichier RTF','Fichier de base de données','Fichier XML','Fichier Debian','Dossier']
FILE_NAME_EN = ['File','No Extension','PDF File','Video File','Archive Folder ','Audio File','Picture File','Link','PYTHON File','PHP File',
'Microsoft Powerpoint Document','HTML File','JAVA File','Desktop Application','Microsoft Excel Document','Style Sheets','C++ File',
'C File','Microsoft Word Document','Text File','Security Certificate','Iso File','Application Extension','Header File','HTM File',
'Log File','PERL File','Paquage','RTF File','Database File','XML File','Debian File','Folder']

COMMON_POPUP_WORDS_FR = ['Fichier en cours d\'utilisation','Ce fichier est actuellement ouvert dans une autre application.\nVeuillez le fermer puis réessayer plus tard.',
						 'Erreur','Ce nom est actuellement utilisé dans ce repertoire.']
COMMON_POPUP_WORDS_EN = ['File already in use','This file is opened in another application.\nPlease close it and try again.',
						 'Error','This name is already used in this directory!']

RENAME_POPUP_FR = ["Renommer","Annuler",
				   "Modification de l'extension","Modifier l'extension du fichier peut l'endommager.\nVoulez-vous le modifier quand même?"]
RENAME_POPUP_EN = ["Rename","Cancel",
				   "Changing extension","Changing a file extension can destroy it.\n Are you sure?"]

NEW_POPUP_FR = ["Nouveau","Fichier","Dossier","Créer","Annuler"]
NEW_POPUP_EN = ["New","File","Folder","Create","Cancel"]

DELETE_POPUP_FR = ["Suppression","Supprimer","Annuler","L\'élément sélectionné sera complètement supprimé de votre ordinateur.\nVoulez-vous le supprimer quand même?"]
DELETE_POPUP_EN = ["Deleting","Delete","Cancel","This will be completly deleted from your computer. Are you sure ?"]

PROPERTIES_POPUP_FR = ["Propriétés de"]
PROPERTIES_POPUP_EN = ["Properties of"]

SETTINGS_POPUP_FR = ["Paramètres"]
SETTINGS_POPUP_EN = ["Settings"]

ABOUT_POPUP_FR = ["A propos de cette application"]
ABOUT_POPUP_EN = ["About this app"]


MAIN_WORDS = []
CONTEXT_MENU = []
LEFT_SIDE_WORDS = []
OTHERS_WORDS = []
FILE_NAME = []
COMMON_POPUP_WORDS = []
RENAME_POPUP = []
NEW_POPUP = []
DELETE_POPUP = []
PROPERTIES_POPUP = []
SETTINGS_POPUP = []


# Here we load every settings variables from the Settings/settings.py file
def loadVariable(filename):
	import imp

	f = open(filename) 
	global data
	data = imp.load_source('data','',f)
	f.close()

# Here we load the language where value is set to true and return its key
def setLang():
	loadVariable(os.path.join(os.path.dirname(os.path.realpath(__file__)),'settings.py'))
	for key,value in data.lang.items():
		if value:
			return key	
"""
# Here we load the theme where value is set to true and return its key
def setTheme():
	loadVariable(os.path.join(os.path.dirname(os.path.realpath(__file__)),'settings.py'))
	for key,value in data.themes.items():
		if value:
			return key
"""

#------------------------------------
#			LANGUAGE SET UP
#------------------------------------
if setLang()=='fr':
	MAIN_WORDS = MAIN_WORDS_FR
	CONTEXT_MENU = CONTEXT_MENU_FR
	LEFT_SIDE_WORDS = LEFT_SIDE_WORDS_FR
	FILE_NAME = FILE_NAME_FR
	OTHERS_WORDS = OTHERS_WORDS_FR
	COMMON_POPUP_WORDS = COMMON_POPUP_WORDS_FR
	RENAME_POPUP = RENAME_POPUP_FR
	DELETE_POPUP = DELETE_POPUP_FR
	NEW_POPUP = NEW_POPUP_FR
	PROPERTIES_POPUP = PROPERTIES_POPUP_FR
	SETTINGS_POPUP = SETTINGS_POPUP_FR
	ABOUT_POPUP = ABOUT_POPUP_FR

elif setLang()=='en':
	MAIN_WORDS = MAIN_WORDS_EN
	CONTEXT_MENU = CONTEXT_MENU_EN
	LEFT_SIDE_WORDS = LEFT_SIDE_WORDS_EN
	FILE_NAME = FILE_NAME_EN
	OTHERS_WORDS = OTHERS_WORDS_EN
	COMMON_POPUP_WORDS = COMMON_POPUP_WORDS_EN
	RENAME_POPUP = RENAME_POPUP_EN
	DELETE_POPUP = DELETE_POPUP_EN
	NEW_POPUP = NEW_POPUP_EN
	PROPERTIES_POPUP = PROPERTIES_POPUP_EN
	SETTINGS_POPUP = SETTINGS_POPUP_EN
	ABOUT_POPUP = ABOUT_POPUP_EN

#------------------------------------
#			THEME SET UP
#------------------------------------