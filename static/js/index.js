function transitions(selector,metal,what) { 
    selector
        .transition()
        .duration(2000)
        .style("opacity",0)
        .transition()
        .duration(2000)
        .style("opacity",1)
        .text(what)
        .transition()
        .duration(2000)
        .style("opacity",0)
        .transition()
        .duration(2000)
        .style("opacity",1)
        .text(metal);
}

d3.json("/moneymaker").then(data => {
    data.forEach((element,index) => {
        if (element < 0) {
            data[index] = "Go Short";
        }
        else {
            data[index] = "Go Long";
        }
    });

    var gold = d3.select("#gold");
    var silver = d3.select("#silver");
    var platinum = d3.select("#platinum");
    var palladium = d3.select("#palladium");

    var initial_1 = gold.text()
    var initial_2 = silver.text()
    var initial_3 = platinum.text()
    var initial_4 = palladium.text()

    transitions(gold,initial_1,data[0]);
    transitions(silver,initial_2,data[1]);
    transitions(platinum,initial_3,data[2]);
    transitions(palladium,initial_4,data[3]);

    setInterval(function() {
        transitions(gold,initial_1,data[0]);
        transitions(silver,initial_2,data[1]);
        transitions(platinum,initial_3,data[2]);
        transitions(palladium,initial_4,data[3]);}, 8000);
});

// function mouseIn() {
//     var temp = d3.select(this)
//     metal = temp.text();
//     var trans = new Promise(
//         function
//     )
//     trans(temp).then(()=>{temp.style("opacity",1).text("hey")})
        
// }

// function mouseOut() {
//     d3.select(this).transition()
//         .duration(2500)
//         .style("opacity",1)
//         .text(metal)
//  }