//  Debugger : print value name and value
var deb = function(nVar, vVar){
	console.log( nVar + " => " + vVar)
};


// Append Skills
var skillsStart = HTMLskillsStart;

var formattedBio = {
	skills : ""
};

for (var skill in bio.skills){
	formattedBio.skills += (HTMLskills.replace("%data%", bio.skills[skill]))
};


formattedBio.headerName = HTMLheaderName.replace("%data%", bio.hName);
formattedBio.role = HTMLheaderRole.replace("%data%", bio.role);
formattedBio.github = HTMLgithub.replace("%data%", bio.contacts.github);
formattedBio.email = HTMLemail.replace("%data%", bio.contacts.email);
formattedBio.gsm = HTMLmobile.replace("%data%", bio.contacts.gsm);
formattedBio.welcomeMsg = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);
formattedBio.bioPic = HTMLbioPic.replace("%data%", bio.bioPic);
formattedBio.skillsStart = HTMLskillsStart;

$("#header").prepend(
		formattedBio.headerName
	+ formattedBio.role
	);
$("#header").append(
		formattedBio.welcomeMsg
	+ formattedBio.bioPic
	+ formattedBio.skillsStart
	);

$("#skills").append(
		formattedBio.skills
	);

$("#topContacts").append(
		formattedBio.github
	+ formattedBio.email
	+ formattedBio.gsm
	);

$("#footerContacts").append(
		formattedBio.github
	+ formattedBio.email
	+ formattedBio.gsm
	);

//WORK
$("#workExperience").append(HTMLworkStart);
for (job in work.jobs){
	$(".work-entry").append(
			HTMLworkEmployer.replace("%data%", work.jobs[job].employer)
		+	HTMLworkTitle.replace("%data%", work.jobs[job].title)
		+ HTMLworkDates.replace("%data%", work.jobs[job].dates)
		+	HTMLworkLocation.replace("%data%", work.jobs[job].location)
		+ HTMLworkDescription.replace("%data%", work.jobs[job].description)
	);
}

// Eductation
$("#education").append(HTMLschoolStart);
for (school in education.schools){
	$(".education-entry").append(
			HTMLschoolName.replace("%data%", education.schools[school].name).replace("#", education.schools[school].url)
		+	HTMLschoolDegree.replace("%data%", education.schools[school].degree)
		+ HTMLschoolDates.replace("%data%", education.schools[school].dates)
		+	HTMLschoolLocation.replace("%data%", education.schools[school].location)
		+ HTMLschoolMajor.replace("%data%", education.schools[school].major)
	);
}

// Online Classes
$("#education").append(HTMLonlineClasses);
$("#education").append(HTMLschoolStart);
for (onlineCourse in education.onlineCourses){
	$(".education-entry").last().append(
		  HTMLonlineTitle.replace("%data%", education.onlineCourses[onlineCourse].title)
		+ HTMLonlineSchool.replace("%data%", education.onlineCourses[onlineCourse].school)
		+ HTMLonlineDates.replace("%data%", education.onlineCourses[onlineCourse].dates)
		+ HTMLonlineURL.replace("%data%", education.onlineCourses[onlineCourse].url).replace("#", education.onlineCourses[onlineCourse].url)
	);
}

// Projects
projects.display = function(){

	for (proj in projects.projects) {
		var images = ""
		if (projects.projects[proj].image.length > 0){
			for (im in projects.projects[proj].image){
				images += HTMLprojectImage.replace("%data%", projects.projects[proj].image[im])
			};
		};

		$("#projects").append(HTMLprojectStart);
		$(".project-entry").last().append(
			  HTMLprojectTitle.replace("%data%", projects.projects[proj].title)
			+ HTMLprojectDates.replace("%data%", projects.projects[proj].date)
			+ HTMLprojectDescription.replace("%data%", projects.projects[proj].description)
			+ images
		);
	};
};

projects.display()

// US/Internationalize Button
$("#main").prepend(usButton);

var usName = function(names){
	var newNames = names.trim().split(" ");
	var newNamesUs = []
	for (var fsName in newNames){
		var nameToChange = newNames[fsName]
		n = nameToChange.charAt(0).toUpperCase() + nameToChange.slice(1).toLowerCase();
		newNamesUs.push(n);
	};
	newNamesUs = newNamesUs.join(" ");
	return(newNamesUs);
};

$(".uButton").click(function(){
	var names = bio["hName"];
	newName = usName(bio["hName"]);
	$("#name").replaceWith(HTMLheaderName.replace("%data%",newName))
});


$("#main").prepend(internationalizeButton);

var inName = function(names){
	var newNames = names.trim().split(" ");
	var fName = newNames[0].charAt(0).toUpperCase() + newNames[0].slice(1).toLowerCase();
	var sName = newNames[1].toUpperCase();
	var newNames = fName + " " + sName;
	return(newNames);
};

$(".iButton").click(function(){
	var names = bio["hName"];
	newName = inName(bio["hName"]);
	$("#name").replaceWith(HTMLheaderName.replace("%data%",newName))
});

// Locations

//   function locationFinder in helper.js does the same job + bio + education
// location map
// var locationizer = function(work_obj){
// 	var locations = [];

// 	for (job in work.jobs){
// 		var newLocation = work_obj.jobs[job].location;
// 		locations.push(newLocation);
// 	}
//  	return(locations);
// }

$("#mapDiv").append(googleMap);

// Click positions logs
$(document).click(function(loc) {
  var x = loc.pageX;
  var y = loc.pageY;
  logClicks(x, y);
});
