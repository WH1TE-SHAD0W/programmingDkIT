def verify_email(email: str):
    email = email.split('@')
    if len(email) == 2:
        if len(email[0]) > 0:
            email[1] = email[1].split('.')
            if len(email[1]) >= 2:
                domain_not_empty_check: bool = True
                for domain in email[1]:
                    if len(domain) == 0:
                        domain_not_empty_check = False
                if domain_not_empty_check:
                    if len(email[1][-1]) >= 2:
                        return True
    return False