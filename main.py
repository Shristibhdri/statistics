from fastapi import FastAPI, Form
import statistics

app = FastAPI()

@app.post("/api/factorial")
async def factorial(num = Form()):
    try:
        num = int(num)
        result = 1
        for a in range(1, num+1):
            result *= a
        return {

    "status": 1,
    "parameter": 3,
    "action": "factorial",
    "result": 6
}
    except ZeroDivisionError as s:
        return{
    "status": 0,
    "message": "Cannot divide by zero."
}
    except Exception as b:
        return{
            "status": 0,
            "message": str(b)
        }
    
@app.post("/api/median")
async def median(num: str = Form()):
    try:
        numbers_list = list(map(float, num.split(',')))
        result = statistics.median(numbers_list)
        return {
            "status": 1,
            "parameter": num,
            "action": "median",
            "result": result
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }
@app.post("/api/variance")
async def population_variance(num: str = Form()):
    try:
        data_list = list(map(float, num.split(',')))
        mean = sum(data_list) / len(data_list)
        variance = sum((x - mean) ** 2 for x in data_list) / len(data_list)

        
        return {
            "status": 1,
            "parameter": num,
            "action": "variance",
            "result": variance
        }
    except ValueError:
        return {
            "status": 0,
            "message": "Invalid input data."
        }
    except ZeroDivisionError:
        return {
            "status": 0,
            "message": "Cannot calculate variance with empty data."
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }
@app.post("/api/pstdev")
async def population_sd(data: str = Form()):
    try:
        numbers_list = [int(num) for num in data.split(',')]
        pstdev = statistics.pstdev(numbers_list)
        
        return {
            "status": 1,
            "parameter": data,
            "action": "population standard deviation",
            "result": pstdev
        }
    except ValueError:
        return {
            "status": 0,
            "message": "Invalid input data."
        }
    except ZeroDivisionError:
        return {
            "status": 0,
            "message": "Cannot calculate standard deviation with empty data."
        }
    except Exception as e:
        return {
            "status": 0,
            "message": str(e)
        }