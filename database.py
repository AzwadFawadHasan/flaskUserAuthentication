# from sqlalchemy import create_engine, text
#
#
# db_connection_string = "mysql+pymysql://devuser:devuser@127.0.0.1:3306/flaskuserauthentication?charset=utf8mb4"
# engine = create_engine(db_connection_string)
#
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row))
#
#     print(result_dicts)
#     # result_all = result.all()
#     # first_result = result_all[0]
#     # first_result_dict = dict(result_all[0])
#     # # print(type(result.all()[0]))
#     # print(type(first_result_dict))
#     # print(result.all())
#
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://devuser:devuser@127.0.0.1:3306/flaskuserauthentication?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = [row._asdict() for row in result]

    print(result_dicts)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [row._asdict() for row in result]

        #print(jobs)
        return jobs

def load_job_from_db(id):
    # with engine.connect() as conn:
    #     result = conn.execute(text("select * from jobs where id = :id"), id=id)
    #     job = [row._asdict() for row in result]
    #
    #     #print(jobs)
    #     if len(job) == 0:
    #         return None
    #     else:
    #         return job
    with engine.connect() as conn:
        query = text("select * from jobs where id = :id")  # Define the query with a named parameter
        result = conn.execute(query, {'id': id})  # Bind the parameter using a dictionary

        job = [row._asdict() for row in result]

        if len(job) == 0:
            return None
        else:
            return job