var a = { name: "rajinikanth", age: 65, industry: "tamil" };
var array1 = [];
var i = 0;
for (var keys in a) {
    array1[i] = keys;
    i++;
}
console.log(array1);
