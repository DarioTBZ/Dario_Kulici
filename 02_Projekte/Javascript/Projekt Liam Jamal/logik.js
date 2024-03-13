var x = 0;
var y = 0;
var zielx = Math.floor(Math.random()*28)*20+20;
var ziely = 500;
var Score = 0;
var Richtung = 0;
//Richtung 1 = links
//  2 = rechts


$(document).ready(function() {
    takt = window.setInterval(taktung,30);
   var spielbrett = document.getElementById("leinwand");
    spielfeld = spielbrett.getContext("2d");
    var spielfigur = new Image();
    Bewegung();
    //Backup ist auf OneNote

    // alles unten löschen
   function Bewegung() {
    if (Richtung = 2) {
        spielfigur.src="spielfigurRechts.png";
        spielfeld.drawImage(spielfigur,x,y)
    }
    else {
        if(Richtung = 1) {
        spielfigur.src="spielfigurLinks.png";
        spielfeld.drawImage(spielfigur.x.y)
        }
    }
   }
   //Hier weitermachen, sodass, wenn Charakter links geht, das Bild auch links gerichtet ist usw. 
   
   //alles oben löschen
    function zeichneZielfeld() {
        var zielfeld = new Image();
        zielfeld.src="zielbereich.png";
        zielfeld.onload=function() {
        spielfeld.drawImage(zielfeld,zielx,ziely);

        }
     }

    function zielfelderreicht() {
        console.log("x: "+x+ "|Ziel x:"+ zielx);
        console.log("y: "+y+ "|Ziel y:"+ ziely);

        if(x==zielx && y==ziely) {
            console.log("Ziel erreicht!");

        
        if (ziely==460) {
            ziely = 0;
        }
        else {
            ziely=460;
        }
        zielx = Math.floor(Math.random()*28)*20+20;
        Score++;
        $("#punktestand").html("Score: "+Score);

        }
    }
    zeichneZielfeld();
  


    function taktung() {
        spielfeld.clearRect(0,0,1800,800);
        zeichneZielfeld();
        spielfeld.drawImage(spielfigur,x,y);
        zielfelderreicht();

    }

    $(document).bind('keydown', function (evt) {
		// console.log(evt.keyCode);
		switch (evt.keyCode) {
			// S
			case 83:
				y += 20;
				if (y >= 600) {
					y = 580;
				}
				// console.log("Wert y: "+y);
				return false;
				break;
			// W
			case 87:
				y -= 20;
				if (y <= 0) {
					y = 0;
				}
				// console.log("Wert -y: "+y);
				return false;
				break;
			// A
			case 65:
				x -= 20;
				if (x <= 0) {
					x = 0;
                    Richtung = 1 //löschen
                    
				}
				// console.log("Wert -x: "+x);
				return false;
				break;
			// D
			case 68:
				x += 20;
				if (x >= 800) {
					x = 780;
                    Richtung = 2 //löschen
                  
				}
				// console.log("Wert x: "+x);
				return false;
				break;
		}	

   

    });

  
    

});  

//68 ist gleich D, 83 für S, 65 für A und 87 für W