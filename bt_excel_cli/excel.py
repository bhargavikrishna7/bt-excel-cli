import pandas
import os

class FileNotFound(Exception):
    pass

class WorkSheetNotFound(Exception):
    pass

class ConditionHeaderNotFound(Exception):
    pass

class Excel:
    
    def __init__(self, path, directory, file_name, sheet_name):
        self.file_name = path + "/" + directory + "/" + file_name

    def __str__(self):
        return "Object created for excel file %s" % (self.file_name)
    
    def __file_exists(self):
        if not os.path.exists(self.file_name):
            return False
        return True

    def __retrieve_worksheets(self):
        if not self.__file_exists():
            raise FileNotFound
        worksheets = pandas.ExcelFile(self.file_name)
        return worksheets.sheet_names
    
    def __validate_worksheet(self, sheet_name):
        worksheets = self.__retrieve_worksheets()
        return False if sheet_name not in worksheets else True
    
    def __read_spreadsheet(self, sheet_name, **kwargs):
        records = pandas.read_excel(self.file_name, sheet_name, kwargs['nrows'])
        return records

    def retrieve_headers(self, sheet_name):
        if not self.__file_exists():
            raise FileNotFound
        if not self.__validate_worksheet(sheet_name):
            raise WorkSheetNotFound
        headers = self.__read_spreadsheet(sheet_name, nrows=0)
        return headers.columns.values

    def retrieve_records(self, sheet_name):
        if not self.__file_exists():
            raise FileNotFound
        if not self.__validate_worksheet(sheet_name):
            raise WorkSheetNotFound
        records = self.__read_spreadsheet(sheet_name, nrows=0)
        return records
    
    def __get_dimensions(self, sheet_name):
        spreadsheet = pandas.ExcelFile(self.file_name)
        df = spreadsheet.parse(sheet_name)
        return df.shape
    
    def __get_row_counts(self, sheet_name):
        return self.__get_dimensions(sheet_name)[0]
    
    def __get_column_counts(self, sheet_name):
        return self.__get_dimensions(sheet_name)[1]
        
    def retrieve_limited_records(self, sheet_name, number_of_rows_retrieved):
        if not self.__file_exists():
            raise FileNotFound
        if not self.__validate_worksheet(sheet_name):
            raise WorkSheetNotFound
        record_count = self.__get_row_counts(
            sheet_name) - number_of_rows_retrieved
        records = self.__read_spreadsheet(
            sheet_name=sheet_name, nrows=record_count)
        return records
        
    def retrieve_records_by_condition(self, sheet_name, **kwargs):
        if not self.__file_exists():
            raise FileNotFound
        if not self.__validate_worksheet(sheet_name):
            raise WorkSheetNotFound
        if all(item in self.retrieve_headers(sheet_name) for item in kwargs.keys()):
            df = self.__read_spreadsheet(sheet_name=sheet_name, nrows=0)
            return df.transpose().to_dict()
        else:
            raise ConditionHeaderNotFound
