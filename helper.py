a="[Behzod + https://validators.readthedocs.io/en/latest/]Akbar-https://validators.readthedocs.io/en/latest[Akbar+https://validators.readthedocs.io/en/latest]"
import validators
def check_url(text):
        havola = ''
        for i in text.split('['):
            for j in i.split(']'):
                if j:

                    if j.rfind('+')!=-1:
                        link  = j[j.rfind('+')+1:]
                        try:
                           validators.url(link)

                           havola+=j+"\n"
                        except Exception as e:
                           print(e)
                    else:
                        pass
                else:
                    pass
        return havola