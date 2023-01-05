# <center>WebService API Traduction</center>
## <center>**Cahier des charges technique**</center>

* ## Sommaire

    1. [Besoins Fonctionnels](#Fonctionnels)

    2. [Besoins techniques](#Techniques)

    3. [API Utilisateur](#Utilisateur)

    4. [API Traduction](#Traduction)

    5. [API Synthèse vocale](#Vocale)

    6. [Front](#Front)

<div style="page-break-after: always; visibility: hidden"> 
</div>

<a name="Fonctionnels"></a>

* ## Besoins Fonctionnels (client)

    Un utilisateur va taper un texte (1000 caractères max) dans une langue de son choix. Provoquer : l'Interrogation d'une api pour connaitre la langue tapée puis une api de traduction qui nous renvoie le texte dans la langue que l'on souhaite et avoir au niveau de l'utilisateur une restitution du langage traduit. 
    Il faut aussi avoir la possibilité de le faire lire par une autre api qui va le convertir en fichier audio

<a name="Techniques"></a>

* ## Besoins techniques

    Tous le projet (informations, API, ... ) est présent sur github à cette addresse : https://github.com/DemonBlueFox/WebService

    Nous allons devélopper une API pour communiquer avec l'utilisateur. Nous utiliserons également des API open source pour traduire le texte envoyer par l'utilisateur ou faire la transcription orale du texte (à travers une synthèse vocale).

    ![](Architecture_des_API.png)
<div style="page-break-after: always; visibility: hidden"> 
</div>

<a name="Utilisateur"></a>

* ### API Utilisateur

    Cette API est développée par nos soins et permet de recupérer les demandent de l'utilisateur sur le front à travers les requêtes HTTP POST et GET. Celle-ci va ensuite utiliser les différentes API de détection de langue, de traduction et de synthèse vocale pour traduire et renvoyer le texte traduit + le fichier audio à l'utilisateur.

<a name="Traduction"></a>

* ### API de traduction
    Pour l'API de traduction, nous utiliserons GoogleTranslate. Pour l'utiliser, il faut d'abord que vous alliez cree votre compte et recuperiez une clé API que vous passez dans la requête GET avec le texte à traduire.

<a name="Vocale"></a>

* ### API de Synthèse Vocale 
    <img src="logo_voicerss.png" alt="logo_voicerss" width="100"/>

    Pour l'API de Synthèse Vocale, l'API [Text-To-Speech](https://www.voicerss.org/api/) par Voicerss est une très bonne solution. Elle permet la retranscription d'un texte à partir d'une requête POST ou GET. 49 langues sont disponibles.

    Cette API possède une requête HTTP POST pour mettre le texte ainsi que la langue dans laquelle on veut traduire et on récupérer le texte traduit.

<a name="Front"></a>

* ### Front
    <img src="VueJS.png" alt="VueJS" width="100"/>

    L'utilisateur aura lui accès à une interface simple. Celle-ci est développé avec vue.js qui permet de faire une application web monopage simple et efficace.