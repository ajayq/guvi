var obj = {name: “ISRO”, age: 35, role: “Scientist”};

function convertListToObject(obj) {
   var array1=[];
  for(let a in obj){
    array1.push([a,obj[a]]);
  }
  console.log(array1);
}
convertListToObject(obj);