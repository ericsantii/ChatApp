from flask import jsonify
from dao.contact import ContactDAO
from handler.person import PersonHandler

class ContactHandler:

    def mapToDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['cID'] = row[1]
        return result

    def getAllContacts(self,pID):
        dao = ContactDAO()
        result = dao.getAllContacts(pID)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Contact=mapped_result)

    def getConctactInfo(self,pid):
        dao = ContactDAO()
        phandler = PersonHandler
        result = dao.getContactInfo(pid)
        mapped_result = []
        for r in result:
            mapped_result.append(phandler.mapToDict(result))
        return jsonify(ContactInfo = mapped_result)