from utils import a2s

class refCollection(object):
    """
    This is a processed version of the Export File for it to be easier 
    processed by python
    """

    class classRefCollection(object):
        """
        Those are the reference for a class
        """
        def __init__(self, token, name):
            self.token = token
            self.name = name
            # three kinds of methods:
            # - virtual
            # - static
            # - interface
            self.methods = None
            # two kinds of fields:
            # - static
            # - instance
            self.fields = None

    def __init__(self, export_file):
        self.export_file = export_file
        self.classes = []

class ProcessedCAPFile(object):
    def __init__(self, cap_file, resolver):
        self.cap_file = cap_file
        self.resolver = resolver
        
    def checkImport(self):
        """
        We check here that all the import package are known
        The parameter is the result of the process of all the export files
        This will return True if all the Import are known.
        """
        for imp in self.cap_file.Import.packages:
            if a2s(imp.aid) not in export_refs:
                return False
        return True

    def checkRefs(self, export_refs):
        """
        We check if the refs from the Constant Pool are to be resolved
        by the export file
        """
        return True

    def extractClasses(self):
        for cls in self.cap_file.Descriptor

if __name__ == "__main__":
    import sys, pickle, capfile, exportfile
    cap = capfile.CAPFile(sys.argv[2])
    pcf = ProcessedCAPFile(cap)
    f = open(sys.argv[1])
    export_refs = pickle.load(f)
    print pcf.checkImport(export_refs)
