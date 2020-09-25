DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS FEEDBACK;

CREATE TABLE user (
  features TEXT PRIMARY KEY,
  context TEXT NOT NULL
  
);

CREATE TABLE post (
  category TEXT PRIMARY KEY,
  context TEXT NOT NULL
);


CREATE TABLE FEEDBACK(
  like_value INTEGER NOT NULL,
  dislike_value INTEGER NOT NULL
);

INSERT INTO post values('graduation',' To meet the requirements for the Master of Science Degree in Electrical Engineering, a student must complete 33 semester units with a cumulative major GPA of 3.0 or better, satisfy competency in written English for Graduate Students and the overall SJSU GPA is 3.0 or better. ');
INSERT INTO post values('electives','You are only allowed to take one course outside the EE graduate courses. for course syllabus please check https://ee.sjsu.edu/content/course-syllabi-for-graduates.  if your overall or candidacy GPA is below  B+ (3.3), then this might lower your GPA you can convert EE295 to CR/NC. Up to 3 units of undergraduate upper-division courses taken in the EE Department at SJSU may be approved as electives, OR Up to 3 units graduate-level courses taken at SJSU but outside the Electrical Engineering Department may be approved as electives, OR Up to 6 units graduate-level Open University courses taken in the EE Department at SJSU (or transferred from another university before your admission to MSEE program at SJSU) may be approved as electives. The Department offers an opportunity to specialize in one of the areas of specialization: Logic/Digital/Embedded System Design, ASIC/VLSI Circuits, Analog/Mixed-Signal Integrated Circuits, Communications/Signal Processing/Machine Learning, Networking, Power Electronics and Control. A student can specialize in an area by taking at least 3 courses in that area. The electives can be taken from the area of specialization or from other areas. A student must consult his/her program advisor to design his/her program of study during the first semester in the department.');
INSERT INTO post values('project','EE 297 (MSEE Project) or EE 299 (Master’s Thesis) is the culminating experience of the MSEE program and may therefore be taken after completing at least 12 units and also must have satisfied the CSU competency in written English requirement, filed the “Candidacy Form”. To register for EE297 or EE299, student must complete the appropriate form from and submit to the EE department for approval');
INSERT INTO post values('others','You can not replace courses in your transcript, All the courses you take show on your transcript and affect your overall GPA. For graduate course advising please contact department graduate adviser Mrs. Birsen Sirkesi');
INSERT INTO FEEDBACK values(0,0);