

function onClickedEstimateRank() {
    console.log("Estimate Closing Rank button clicked");
    var year = document.getElementById("uiYear");
    console.log(year);
    var institute = document.getElementById("uiInstitute");
    
    
    var department = document.getElementById("uiDepartment");
    var degree = document.getElementById("uiDegree");

    var category = document.getElementById("uiCategory");
    var pool = document.getElementById("uiPool");
    var program_duration = document.getElementById("uiProgramDuration");


    var estimatedRank = document.getElementById("uiEstimatedRank");

    console.log("Estimate Closing Rank button clicked");
  
    // var url_predict = "http://127.0.0.1:5000/predictCrank"; //Use this if you are NOT using nginx 
   var url_predict = "/api/predictCrank"; // Use this if  you are using nginx. 
  
    console.log("Estimate Closing Rank button clicked");
    $.post(url_predict, {
        year: parseFloat(year.value),
        pool: pool.value,
        program_duration: program_duration.value,
        degree_name: degree.value,
        institute_name: institute.value,
        category: category.value,
        department: department.value
        
        
        
        

    },function(data, status) {
        console.log(data.predictedCrank);
        estimatedRank.innerHTML = "<h2> Closing Rank for your search is : " + data.predictedCrank.toString() + "</h2>";
        console.log(status);
    });
  }
  




function onPageLoad() {
    console.log( "document loaded" );

    // var url_inst = "http://127.0.0.1:5000/get_instituteName"; // Use this if you are NOT using nginx 
   var url_inst = "/api/get_instituteName"; // Use this if  you are using nginx. 
    $.get(url_inst,function(data, status) {
        console.log("got response for get_instituteName request");
        if(data) {
            var institutes = data.institute_name;
            var uiInstitute = document.getElementById("uiInstitute");
            $('#uiInstitute').empty();
            for(var i in institutes) {
                var opt = new Option(institutes[i]);
                $('#uiInstitute').append(opt);
            }
        }
    });


    //  var url_depart = "http://127.0.0.1:5000/get_department_name"; // Use this if you are NOT using nginx 
   var url_depart = "/api/get_department_name"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url_depart,function(data, status) {
        console.log("got response for get_department_name request");
        if(data) {
            var departments = data.department;
            var uiDepartment = document.getElementById("uiDepartment");
            $('#uiDepartment').empty();
            for(var i in departments) {
                var opt = new Option(departments[i]);
                $('#uiDepartment').append(opt);
            }
        }
    });


    //  var url_degree = "http://127.0.0.1:5000/degree_name"; // Use this if you are NOT using nginx which is first 7 tutorials
   var url_degree = "/api/degree_name"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url_degree,function(data, status) {
        console.log("got response for degree_name request");
        if(data) {
            var degrees = data.degree_name;
            var uiDegree = document.getElementById("uiDegree");
            $('#uiDegree').empty();
            for(var i in degrees) {
                var opt = new Option(degrees[i]);
                $('#uiDegree').append(opt);
            }
        }
    });


    //  var url_cat = "http://127.0.0.1:5000/get_category"; // Use this if you are NOT using nginx which is first 7 tutorials
   var url_cat = "/api/get_category"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url_cat,function(data, status) {
        console.log("got response for get_category request");
        if(data) {
            var categories = data.category;
            var uiCategory = document.getElementById("uiCategory");
            $('#uiCategory').empty();
            for(var i in categories ) {
                var opt = new Option(categories[i]);
                $('#uiCategory').append(opt);
            }
        }
    });


    

    //  var url_pool = "http://127.0.0.1:5000/get_pool"; // Use this if you are NOT using nginx which is first 7 tutorials
   var url_pool = "/api/get_pool"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url_pool,function(data, status) {
        console.log("got response for get_pool request");
        if(data) {
            var pools = data.pool;
            var uiPool = document.getElementById("uiPool");
            $('#uiPool').empty();
            for(var i in pools) {
                var opt = new Option(pools[i]);
                $('#uiPool').append(opt);
            }
        }
    });

    //  var url_progDur = "http://127.0.0.1:5000/get_program_duration"; // Use this if you are NOT using nginx which is first 7 tutorials
   var url_progDur = "/api/get_program_duration"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url_progDur,function(data, status) {
        console.log("got response for get_program_duration request");
        if(data) {
            var durations = data.program_duration;
            var uiProgramDuration = document.getElementById("uiProgramDuration");
            $('#uiProgramDuration').empty();
            for(var i in durations) {
                var opt = new Option(durations[i]);
                $('#uiProgramDuration').append(opt);
            }
        }
    });



    
  }
  
  window.onload = onPageLoad;