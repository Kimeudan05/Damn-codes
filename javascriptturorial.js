// //for in loop
// const person = {fname:"John", lname:"Doe", age:25}; 

// let txt = "";
// for (let x in person) {
//   txt = txt + person[x] + " ";
// }
// console.log(txt);

// //for of
// const cars = ["BMW", "Volvo", "Mini"];

// let tet = "";
// for (let x of cars) {
//   tet += x;
// }
// console.log(tet)

// const caris = ["BMW", "Volvo", "Saab", "Ford"];
// let i = 0;
// let text = "";

// while (caris[i]) {
//   text += caris[i];
//   i++;
// }
// console.log(caris)

// //break and continue
// for (let i = 0; i < 10; i++) {
//     if (i === 3) { continue; }
//     console.log(i);
//   }

function checkValue(){
    var fruit=document.getElementById("fruits").value;

    switch(fruit){
        case "joker":
            var amount ="e12.3$";
            document.getElementById("demo").innerHTML="The price of " +fruit +" is "+amount;
            break;
        case "sugar":
            var amount ="e12.3$";
            document.getElementById("demo").innerHTML="The price of " +fruit +" is "+amount;
            break;
        case "salt":
             var amount ="e12.3$";
            document.getElementById("demo").innerHTML="The price of " +fruit +" is "+amount;
             break;
        case "maximum":
            var amount="3.3$";
            document.getElementById('demo').innerHTML="The price of " +fruit +" is "+amount;
            break;
        default:
            document.getElementById('demo').innerHTML="Fruit curently available in the store";

    }
}
  
 
  