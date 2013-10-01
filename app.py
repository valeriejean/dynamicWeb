import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template

app = Flask(__name__)

members = {}
members['Fangyun']= {
	'role' : 'MA' ,
	'image':'fangyun.jpg',
	'nickname':'Frances',
	'birthyear' : 1956 ,
	'job' : 'Rite Aid pharmacist' ,
	'pronoun' : 'She' ,
	'likes' : "consuming tamales & strong margaritas, going to the movies, buying clothes for her granddaughter, and getting good deals at Macys via clever use of coupons" ,
	'tradition' : "we go to Starbucks together and drink coffees and share a pastry. She always tells me my drink is too sweet and that I need to stop grimacing when I talk because I'm distorting the muscles in my face"
}
members['Shienkun']= {
	'role' : 'PA' ,
	'image':'shienkun.jpg',
	'nickname':'Jerry',
	'birthyear' : 1952 ,
	'job' : "stock investor" ,
	'pronoun' : 'He' ,
	'likes' : "gardening, meditating, learning about Chinese medicine, performing small domestic tasks, talking about the probable existence of aliens, and photography" ,
	'tradition' : "we go to Souplantation in Orange County, just the two of us, and we've carried out the our shared buffet rituals for as long as I can remember. He gets my soup for me and it's always clam chowder or chicken noodle and we always share one piece of cornbread"
}
members['Clifford']= {
	'role' : 'OH BROTHER' ,
	'image':'clifford.jpg',
	'nickname':'Cliff',
	'birthyear' : 1980 ,
	'job' : "software engineer" ,
	'pronoun' : 'He' ,
	'likes' : "mountain biking, listening to jazz music, playing saxopohone and trombone, buying the newest Apple products, and flying RC helicopters" ,
	'tradition' : "we don't have one and that's sad. We get along but our eight-year age difference has really inhibited our closeness"
}
members['Rosemary']= {
	'role' : 'SIS-IN-LAW' ,
	'image':'rosemary.jpg',
	'nickname':'Rosie',
	'birthyear' : 1980 ,
	'job' : 'CPA' ,
	'pronoun' : 'She' ,
	'likes' : "listening to country music, voting on American Idol, eating chicken Mcnuggets, and drinking Starbucks" ,
	'tradition' : "she always takes me out for boba after we have dimsum with my parents"
}
members['Charlotte']= {
	'role' : 'NEWEST CHEN' ,
	'image':'charlotte.jpg',
	'nickname':'Char',
	'birthyear' : 2012 ,
	'job' : 'baby' ,
	'pronoun' : 'She' ,
	'likes' : "getting attention, hugging stuffed animals, and being photographed" ,
	'tradition' : "she sits in my lap, sometimes pulls my hair"
}

@app.route('/')
def mainpage():
	#returning just one variable
	#message = 'These are a few of my favorite things'
	#return render_template('index.html', message=message)

	return render_template('index.html', members = members)
	#return render_template('index.html', **templateData)
	#the operator in Python will convert a dictionary into a keyword list
	#return render_template{'index.html', message = 'A few of my favorite things', a_sentence = '...'}

@app.route("/thischen", methods = ["POST"])
def thischen():

	# Get the user submitted data
	selectedPersonData = {
		'member_name' : request.form.get('member')
	}

	# get animal by animal_name 
	selectedPersonData['member'] = members[ selectedPersonData.get('member_name') ]

	return render_template("thischen.html", **selectedPersonData)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)