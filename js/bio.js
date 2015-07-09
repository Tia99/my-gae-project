var bio = {
    		"name":"Tatiana",
    		"role":"Udacity student",
    		"skills":["making friends", "reading somebody's mind", "learning foreign languages"],
    		"welcomepage": "Thank you for visiting my page!"

    	};
$("#main").append("<p>"+bio.welcomepage+"</p>");
console.log(bio.welcomepage);

var profile = {
	"skills":
		{
		"hobby":"creative writing",
		"music":"playing the piano",
		"sports":"yoga",
		"foreign languages":["Italian", "German", "Russian"]
		},
	"education": [
		{
		"majors": ["Linguistics", "English language", "English literature"],
		"courses": ["Creative Writing", "Italian"],
		"onlinecourses":"Introduction to Programming"
		}
	]
};
$("#main").append("<p>"+profile.education[0].onlinecourses+"</p>");
console.log(profile.education[0].onlinecourses);