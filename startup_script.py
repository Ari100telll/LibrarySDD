from services.observer.librarian import Librarian
from services.observer.library_publisher import LibraryPublisher


def setup_librarian():
    librarian = Librarian()
    library_publisher = LibraryPublisher()

    library_publisher.subscribe(librarian)


def run_startup_script():
    setup_librarian()
