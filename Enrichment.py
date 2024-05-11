import json
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    filtered_data = []
    try:
        for i in event:
            data = json.loads(i['body']) 
            if (data['startDate'] == data['endDate']):
                continue
            else:
                filtered_data.append(data)
        
        logger.info("Current batch completed!")
    except Exception as e:
        logger.exception('An error occurred: %s', e)
        
    return filtered_data