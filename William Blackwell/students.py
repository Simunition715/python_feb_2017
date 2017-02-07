kind = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def theNames(info, title):

	print title


	for i in range(len(info)):

		full_name = info[i]['first_name'] + " " + info[i]['last_name']

		print (i + 1), "-", full_name, "-", (len(full_name) - 1)

students = kind['Students']
instructors = kind['Instructors']

theNames(students, 'Students')
theNames(instructors, 'Instructors')