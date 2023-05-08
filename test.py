import pymongo
import unittest

class TestJobDescriptions(unittest.TestCase):
    def test_existingJobDescriptions(self):
        # Connect to MongoDB
        conn_str = "mongodb://project3343:rsproject@ac-gjl3aea-shard-00-00.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-01.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-02.sop0wqm.mongodb.net:27017/?ssl=true&replicaSet=atlas-xr3bsz-shard-0&authSource=admin&retryWrites=true&w=majority"
        client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        db = client.resumeDB
        jd = db.jd

        # Sample job description to check
        sample_job_description = "SYSTEM ENGINEER  at google, 2 years of experience in workspace environment , CGPA:8.0, major knowledge in technical understanding Installing, configuring, testing and maintaining operating system s, application software and system management tools  has major skills in it Must be a part of Google hackathon  Python C C++ Kotlin"

        # Check if the sample job description is present in MongoDB
        result = jd.find_one({"desc": sample_job_description})
        self.assertIsNotNone(result, f"Job description '{sample_job_description}' not found in MongoDB")

if __name__ == '__main__':
    unittest.main()
