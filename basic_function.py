# *************************************************************************** #
#                                                                              #
#    basic_function.py                                                         #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/12/21 16:58:19 by Widium                                    #
#    Updated: 2023/12/21 16:58:19 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from logger import AdvancedLogger
from langchain.docstore.document import Document

def get_document():
    text = "This is the raw text content of the document"
    metadata = {"source": "http://example.com/document.txt"}
    document = Document(page_content=text, metadata=metadata)
    AdvancedLogger.log_object(document)
    
    return document
