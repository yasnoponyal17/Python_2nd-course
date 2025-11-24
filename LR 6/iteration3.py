import logging
from currencies import get_currencies

logging.basicConfig(
    filename="currencies.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger("currency_api")

def get_currencies_logging(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    logger.info(f"Codes: {currency_codes}")
    
    try:
        result = get_currencies(currency_codes, url)
        
        if result is None:
            logger.error("API returned invalid data or a request error occurred")
        else:
            not_found = [code for code in currency_codes if code not in result]
            for code in not_found:
                logger.warning(f"Code '{code}' was not found.")
            
            logger.info(f"Number of exchange rates received: {len(result)}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error while executing request: {e}")
        return None

result = get_currencies_logging(['USD', 'EUR', 'BYN', 'KEK'])
print("Результат:", result)