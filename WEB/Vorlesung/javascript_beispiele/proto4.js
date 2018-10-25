class Rectangle {
   constructor (length, width) {          
      this.length = length; 
      this.width = width; 
   } 
   getArea () { 
      return this.length * this.width; 
   } 
   toString () { 
      return "[Rectangle " + this.length + "x" + this.width + "]"; 
   } 
}

// Erbt von Rectangle 
class Square extends Rectangle {
   constructor (size) {
      super(size, size);  // Aufruf des Basisklassen-Constructor
   } 
   toString () { 
      return "[Square " + this.length + "x" + this.width + "]"; 
   } 
} 

var rect = new Rectangle(5, 10); 
var square = new Square(6); 

console.log(rect.getArea());                 // 50 
console.log(square.getArea());               // 36 
console.log(rect.toString());                // "[Rectangle 5x10]" 
console.log(square.toString());              // "[Square 6x6]" 
console.log(rect instanceof Rectangle);      // true 
console.log(rect instanceof Object);         // true 
console.log(square instanceof Square);       // true 
console.log(square instanceof Rectangle);    // true 
console.log(square instanceof Object);       // true
