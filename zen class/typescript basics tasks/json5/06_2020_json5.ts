var arr1 = [['make', 'Ford'], ['model', 'Mustang'], ['year', 1964]];
var myobj={};
arr1.forEach(function(array){
    myobj[array[0]]=array[1];

})
console.log(myobj);