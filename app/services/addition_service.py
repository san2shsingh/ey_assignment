import logging
from multiprocessing import Pool
from typing import List

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s [%(processName)s] %(message)s',
    handlers=[
        logging.FileHandler("multiprocessing_addition.log"),
        logging.StreamHandler()
    ]
)

def add_numbers(numbers: List[int]) -> int:
    try:
        logging.debug(f"Received list for addition: {numbers}")
        result = sum(numbers)
        logging.debug(f"Sum of {numbers} is {result}")
        return result
    except Exception as e:
        logging.error(f"Error processing list {numbers}: {e}")
        raise

def process_additions(lists_of_numbers: List[List[int]]) -> List[int]:
    with Pool() as pool:
        results = pool.map(add_numbers, lists_of_numbers)
    return results
