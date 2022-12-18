from colored import  fore, style


def throw_card_prompt():
    
    prompt = input(fore.GREEN_YELLOW + style.BOLD +"Please type in the card you would like to throw: ").lower()
    return prompt




