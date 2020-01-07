var object1 = { name: "rajinikanth", industry: "tamil" };
var array1 = [];
var i = 0;
for (var prop in object1) {
    array1[i] = object1[prop];
    i++;
}
console.log(array1);
