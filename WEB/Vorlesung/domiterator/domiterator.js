// Konstruktor
//    Parameter : DOM-Knoten, der als Ausgangspunkt dient
function DOMIterator (Root) {
   this.Root  = Root;       // speichert Ausgangspunkt
   this.Node  = this.Root;  // der aktuelle Knoten
   this.Level = 0;          // die aktuelle Tiefe
   this.Dir   = 0;          // dient der Steuerung
   this.Show  = false;      // dient der Steuerung

   // Zugriff auf den ersten Knoten
   this.First = function () {
      this.Node  = this.Root;
      this.Level = 0;
      this.Dir   = 0;
      this.Show  = false;
      return this.Node;
   }

   // Zugriff auf den naechsten Knoten
   this.Next = function () {
      while (this.Node != null) {
         if (this.Show) {
            this.Show = false;
            break;
         }
         switch (this.Dir) {
         case 0:
            if (this.Node.firstChild != null) {
               this.Node = this.Node.firstChild;
               this.Show  = true;
               this.Level++;
            } else {
               this.Dir   = 1;
            }
            break;
         case 1:
            if (this.Node === this.Root) {
               // Ausgangspunkt erreicht
               this.Node = null;
            } else {
               if (this.Node.nextSibling != null) {
                  this.Node = this.Node.nextSibling;
                  this.Dir   = 0;
                  this.Show  = true;
               } else {
                  this.Dir   = 2;
               }
            }
            break;
         case 2:
            if (this.Node === this.Root) {
               // Ausgangspunkt erreicht
               this.Node = null;
            } else {
               this.Node = this.Node.parentNode;
               if (this.Node === this.Root) {
                  // Ausgangspunkt erreicht
                  this.Node = null;
               }
               this.Level--;
            }
            this.Dir = 1;
            break;
         }
      }
      return this.Node;
   }
}
