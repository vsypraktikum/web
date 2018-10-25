function Rectangle(length, width) {          
   this.length = length; 
   this.width = width; 
} 

Rectangle.prototype.getArea = function() { 
   return this.length * this.width; 
}; 

Rectangle.prototype.toString = function() { 
   return "[Rectangle " + this.length + "x" + this.width + "]"; 
}; 

// Erbt von Rectangle 
function Square(size) {                      
   this.length = size; 
   this.width = size; 
} 

Square.prototype = new Rectangle();          // (1)
Square.prototype.constructor = Square;       // (2)

Square.prototype.toString = function() { 
   return "[Square " + this.length + "x" + this.width + "]"; 
}; 

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
