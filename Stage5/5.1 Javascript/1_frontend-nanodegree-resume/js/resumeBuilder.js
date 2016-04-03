/*
This is empty on purpose! Your code to build the resume will go here.
 */

 // var awesomeThoughts = "I am a budgie and I am AWESOME!";
 // console.log(awesomeThoughts);
 // var funThoughts = awesomeThoughts.replace("AWESOME","FUN");
 // console.log(funThoughts);
 // $("#main").append(" This is me :) " + funThoughts);



// TODO
// Move contacts in topcontact div
var bio = {
	"name" : "Camille Gabrieli",
	"role" : "Developer",
	"contacts" : {
		"github" : "https://github.com/aziaziazi",
		"email" : "camille.gabrieli@gmail.com",
		"gsm" : "0491528267",
		"location" : "Brussels"
	},
	"welcomeMessage" : "Thanks for reading my resume!",
	"skills" : [
		"product design", "front end", "3d printing"
		],
	"bioPic" : "images/fry.jpg"
};

var work = {
	"works" : [
		{
			"employer" : "Freelance",
			"title" : "Designer",
			"dates" : "January 2013 - Future",
			"location" : "Bruxelles",
			"description" : "Exploring the FabLab and exploring the FabLab and exploring the FabLab and exploring the FabLab and exploring the FabLab"
		},
		{
			"employer" : "AREP",
			"title" : "Designer",
			"dates" : "2009 - 2012",
			"location" : "Paris",
			"description" : "Transportation stuff, orientation guide and waiting funmaker"
		}
	]
};

//EDUCATION
var education = {
	"schools" : [
		{
			"name" : "École Boulle",
			"degree" : "Diplôme des Métiers d'Art",
			"dates" : 2009,
			"location" : "Paris",
			"major" : "Ébénisterie",
			"url" : "http://www.ecole-boulle.org/"

		},
		{
			"name" : "LEP Revel",
			"degree" : "Bac Pro",
			"dates" : 2007,
			"location" : "Revel",
			"major" : "Ébénisterie",
			"url" : "http://ameublement-revel.entmip.fr/"
		}
	],
	"onlineCourses" : [
		{
			"title" : "Intro to Programming",
			"school" : "Udacity",
			"dates" : 2016,
			"url" : "https://www.udacity.com/course/intro-to-programming--ud000"
		}
	]
};

var project = {
	"projects" : [
		{
			"title" : "pinhole camera",
			"date" : "2014",
			"description" : "this is a carboard analogic camera",
			"image" : "images/197x148.gif"
		},
			{
			"title" : "pocessing workshop",
			"date" : "2015",
			"description" : "interactive color spawner",
			"image" : "images/output-113.png"
		}
	]
};


var skillsStart = HTMLskillsStart;

var formattedBio = {
	skills : ""
};

for (i=0; i < bio.skills.length; i++){
	formattedBio.skills += (HTMLskills.replace("%data%", bio.skills[i]))
};


formattedBio.headerName = HTMLheaderName.replace("%data%", bio.headerName);
formattedBio.role = HTMLheaderRole.replace("%data%", bio.role);
formattedBio.github = HTMLgithub.replace("%data%", bio.github);
formattedBio.email = HTMLemail.replace("%data%", bio.email);
formattedBio.welcomeMsg = HTMLwelcomeMsg.replace("%data%", bio.welcomeMsg);
formattedBio.bioPic = HTMLbioPic.replace("%data%", bio.bioPic);
formattedBio.skillsStart = HTMLskillsStart;
console.log("HTMLskillsStart = "+HTMLskillsStart)
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
	);

//WORK

$("#workExperience").append(HTMLworkStart);

$(".work-entry").append(
		HTMLworkEmployer.replace("%data%", work.workEmployer)
	+	HTMLworkTitle.replace("%data%", work.workTitle)
	+ HTMLworkDates.replace("%data%", work.workDates)
	+	HTMLworkLocation.replace("%data%", work.workLocation)
	+ HTMLworkDescription.replace("%data%", work.workDescription)
);



$("#education").append(HTMLschoolStart);

$(".education-entry").append(
		HTMLschoolName.replace("%data%", education["schoolName"])
	+	HTMLschoolDegree.replace("%data%", education["schoolDegree"])
	+ HTMLschoolDates.replace("%data%", education["schoolDates"])
	+	HTMLschoolLocation.replace("%data%", education["schoolLocation"])
	+ HTMLschoolMajor.replace("%data%", education["schoolMajor"])
);