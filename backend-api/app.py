from flask import Flask, request    
from uuid import uuid4   
from flasgger import Swagger
from datetime import datetime
database = {}

app = Flask(__name__) # creating an instance of the Flask class and passing in the name of the current module as an argument. This will allow us to create routes and handle requests for our web application.
swagger = Swagger(app)

@app.route("/", methods=["GET","POST"], endpoint="homepage") 
def home():
    return "Welcome to my learning hub!"

@app.post("/v1/ct")
def create_table():
    data = request.get_json()
    table_name = data.get("table_name")
    if not table_name:
        return {"message": "Table name is required!"}, 400
    database[table_name] = {}

    return {
    "message": "Database created successfully!" , "status": 205 , "database": database 
    }
@app.post("/v1/uc")
def create_user():
    data = request.get_json()
    table_name = data.get("table_name")
    user_id = str(uuid4())  # here we are generating a unique user ID using the uuid4() function from the uuid module. This will ensure that each user has a unique identifier.
    user_name = data.get("user_name")
    email_id = data.get("email_id")
    if not table_name or not user_id:
        return {"message": "Table name and user ID are required!"}, 400
    if table_name not in database:
        return {"message": f"Table '{table_name}' does not exist!"}, 404
    database[table_name][user_id] = {"user_name": user_name, "email_id": email_id }

    return {
        "message": f"User '{user_id}' created successfully in table '{table_name}'!",
        "status": 201,
        "database": database
    }

@app.get("/v1/fu/<table_name>/<uid>")
def find_user_by_email(table_name, uid):
  """
    Find a user by email ID in the specified table.
    ---
    parameters:
    -  name: table_name
       in : path
       type: string
       required: true
       description: "Its name of the db table"
    -  name: uid
       in : path
       type: string
       required: true
       description: "Its the id of each row"
    responses:
       200:
           description: "Successfully retrieved the table name"
       500:
           description: "Internal server error"
  """
  if uid in database[table_name]:
    email_id = database[table_name][uid]["email_id"]
    return {"table_name": table_name, "user_id": uid, "user_data": database[table_name][uid]}, 200

    #for table_name, users in database.items():
        #for user_id, user_data in users.items():
            #if user_data.get("email_id") == email_id:
                #return {"table_name": table_name, "user_id": user_id, "user_data": user_data}
    #print(email_id)
    #return {"message": f"User with email ID '{email_id}' not found!"}, 404

@app.get("/gt")
def get_all_users():
    return {"database": database}, 200

@app.route("/v1/testimonials", methods=["POST"])
def create_testimonial():
    """
    Create a new testimonial.
    ---
    parameters:
    -  name: author_name
       in : path
       type: string
       required: true
       description: "Name of the author"
    -  name: content
       in : path
       type: string
       required: true
       description: "Content of the testimonial"
    -  name: rating
       in : path
       type: integer
       required: true
       description: "Rating for the testimonial"
    -  name: status
       in : path
       type: string
       required: true
       description: "Status of the testimonial"
    responses:
       201:     
              description: "Testimonial created successfully"
       500:
              description: "Internal server error"
"""
    data = request.get_json()
    print(data)  # here we are printing the data received in the request to the console. This is useful for debugging purposes and allows us to see what data is being sent to the server.
    # Process the testimonial data
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(created_at)  # here we are printing the current date and time to the console. This is useful for debugging purposes and allows us to see when the testimonial was created.
    author = data.get("author_name")
    content = data.get("content")
    rating = data.get("rating")
    status = data.get("status")
    database["testimonials"] = {
        "id": uuid4().hex,
        "author_name": author,
        "content": content,
        "rating": rating,
        "status": status,
        "created_at": created_at
            }
    return {"message": "Testimonial created successfully!"}, 201

@app.route("/v1/courses", methods=["POST"])
def create_course(): 
    """
    Create a new course.
    ---
    parameters:
    -  name: title
       in : path
       type: string
       required: true
       description: "Title of the course"
    -  name: description
       in : path
       type: string    
       required: true
       description: "Description of the course"
    -  name: category
       in : path
       type: string
       required: true
       description: "Category of the course"
    -  name: level
       in : path
       type: string
       required: true
       description: "Level of the course"
    -  name: status
       in : path   
       type: string
       required: true  
       description: "Status of the course"
    responses:
         201:     
                  description: "Course created successfully"
         500:
                  description: "Internal server error"          
"""
    data = request.get_json()
    print(data)
    title = data.get("title")
    description = data.get("description")
    category = data.get("category")
    level = data.get("level")
    status = data.get("status")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_by = data.get("created_by")
    database["courses"] = {
        "id": uuid4().hex,
        "title": title,
        "description": description,
        "category": category,
        "level": level,
        "status": status
            }
    return {"message": "Course created successfully!"}, 201

@app.route("/v1/membershipplans", methods=["POST"])
def create_membership_plan():
    """
    Create a new membership plan.
    ---
    parameters:
    -  name: name
       in : path
       type: string
       required: true
       description: "Name of the membership plan"
    -  name: description
       in : path
       type: string
       required: true
       description: "Description of the membership plan"
    -  name: currency
       in : path   
       type: string
       required: true
       description: "Currency of the membership plan"
    -  name: duration       
       in : path
       type: string
       required: true
       description: "Duration of the membership plan"
    -  name: features
       in : path
       type: string
       required: true
       description: "Features of the membership plan"
    -  name: status 
       in : path
       type: string
       required: true
       description: "Status of the membership plan"
    responses:
       201:   
          description: "Membership plan created successfully"
       500:            
          description: "Internal server error"   
"""
    data = request.get_json()
    print(data)
    name = data.get("name") 
    description = data.get("description")
    currency = data.get("currency")
    duration = data.get("duration")
    features = data.get("features")
    status = data.get("status")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    database["membershipplans"] = {
        "id": uuid4().hex,
        "name": name,
        "description": description,
        "currency": currency,
        "duration": duration,
        "features": features,
        "status": status
            }
    return {"message": "Membership plan created successfully!"}, 201

@app.route("/v1/qa", methods=["PUT"])
def create_qa():
    """
    Create a new Q&A entry.
    --- 
    parameters:
    -  name: question
       in : path
       type: string
       required: true
       description: "Question for the Q&A entry"
    -  name: answer
       in : path
       type: string
       required: true
       description: "Answer for the Q&A entry"
    -  name: asked_by
       in : path
       type: string
       required: true
       description: "Person who asked the question"
    -  name: answered_by
       in : path
       type: string
       required: true
       description: "Person who answered the question"
    -  name: status 
       in : path
       type: string
       required: true
       description: "Status of the Q&A entry"
    responses:
       201: 
          description: "Q&A entry created successfully"
       500:
          description: "Internal server error"
"""
    data = request.get_json()
    print(data)
    question = data.get("question")
    answer = data.get("answer")
    asked_by = data.get("asked_by")
    answered_by = data.get("answered_by")
    status = data.get("status")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    database["qa"] = {
        "id": uuid4().hex,
        "question": question,
        "answer": answer,
        "asked_by": asked_by,
        "answered_by": answered_by,
        "status": status
            }
    return {"message": "Q&A created successfully!"}, 201


print(app.url_map)
print(app.view_functions)   

if __name__ == "__main__":
    app.run(debug=True)

