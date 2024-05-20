import logging

def find_element(soup_element, tag_name, attribute_name=None, attribute_value=None):
    if not soup_element:
        raise Exception('Soup Element not found')

    if not tag_name:
        raise Exception('Tag name not found')

    if not attribute_name or not attribute_value:
        element = soup_element.find(tag_name)
        if element:
            return element
        return None
    try:
        return soup_element.find(tag_name, attrs={f'{attribute_name}': attribute_value})
    except Exception as e:
        message = f'Failed to find {tag_name}: {e}'
        logging.error(message)
        raise Exception(message)
    
def find_all_elements(soup_element, tag_name, attribute_name=None, attribute_value=None):
    if not soup_element:
        raise Exception('Soup HTML not found')

    if not tag_name:
        raise Exception('Tag name not found')

    if not attribute_name or not attribute_value:
        elements = soup_element.findAll(tag_name)
        if elements:
            return elements
        return []
    try:
        return soup_element.findAll(tag_name, attrs={f'{attribute_name}': attribute_value})
    except Exception as e:
        message = f'Failed to find {tag_name}: {e}'
        logging.error(message)
        raise Exception(message)
    