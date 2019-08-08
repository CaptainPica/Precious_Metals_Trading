pathing = d3.select("#typing").text();
chart_pathing = pathing.toUpperCase()

dl_pic = d3.select("#DLGraph").append("img")
    .attr("alt","Deep Learning Equity Curve")
    .attr("src",`/static/images/${chart_pathing}_DL_EC.png`)

rf_pic = d3.select("#RFGraph").append("img")
    .attr("alt","Random Forest Equity Curve")
    .attr("src",`/static/images/${chart_pathing}_RF.png`)

d3.json(`/tableinfo/${pathing}`).then(data => {
    dl_head = d3.select("#DL > thead")
    dl_body = d3.select("#DL > tbody")
    rf_head = d3.select("#RF > thead")
    rf_body = d3.select("#RF > tbody")

    dl_head.html("")
    dl_body.html("")
    rf_head.html("")
    rf_body.html("")

    var dl_row_head = dl_head.append("tr");
    data["DL"]["columns"].forEach(element => {
        dl_row_head.append("th").text(element);
    });

    data["DL"]["data"].forEach(element => {
        let dl_row_body = dl_body.append("tr");
        element.forEach(segment => {
            dl_row_body.append("td").text(segment)
        });
    });

    var rf_row_head = rf_head.append("tr");
    data["RF"]["columns"].forEach(element => {
        rf_row_head.append("th").text(element);
    });

    data["RF"]["data"].forEach(element => {
        let rf_row_body = rf_body.append("tr");
        element.forEach(segment => {
            rf_row_body.append("td").text(segment)
        });
    });
});