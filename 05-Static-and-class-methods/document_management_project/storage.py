class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join(doc.__repr__() for doc in self.documents)

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for x in self.categories:
            if x.id == category_id:
                x.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for x in self.topics:
            if x.id == topic_id:
                x.topic = new_topic
                x.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for x in self.documents:
            if x.id == document_id:
                x.file_name = new_file_name

    def delete_category(self, category_id):
        for x in self.categories:
            if x.id == category_id:
                self.categories.remove(x)

    def delete_topic(self, topic_id):
        for x in self.topics:
            if x.id == topic_id:
                self.topics.remove(x)

    def delete_document(self, document_id):
        for x in self.documents:
            if x.id == document_id:
                self.documents.remove(x)

    def get_document(self, document_id):
        for x in self.documents:
            if x.id == document_id:
                return x


from document_management_project.category import Category
from document_management_project.document import Document
from document_management_project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize document_management_project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)

# Category 1: work
# Topic 1: daily tasks in C:\work_documents
# Document 1: finilize document_management_project; category 1, topic 1, tags: urgent, work
# Document 1: finilize document_management_project; category 1, topic 1, tags: urgent, work
