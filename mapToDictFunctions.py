def mapGroupToDict(self, row):
    result = {}
    result['gID'] = row[0]
    result['gName'] = row[1]
    result['pID'] = row[2]
    return result


def mapMessageToDict(self, row):
    result = {}
    result['mID'] = row[0]
    result['mText'] = row[1]
    result['timedate'] = row[2]
    result['multimedia'] = row[3]
    result['pID'] = row[4]
    result['gID'] = row[5]
    return result


def mapPersonToDict(self, row):
    result = {}
    result['pID'] = row[0]
    result['pFirstName'] = row[1]
    result['pLastName'] = row[2]
    result['username'] = row[3]
    result['password'] = row[4]
    result['pPhone'] = row[5]
    result['pEmail'] = row[6]
    return result

def mapHashTagToDict(self, row):
    result = {}
    result['hID'] = row[0]
    result['hText'] = row[1]
    result['mID'] = row[2]
    return result

def mapToReactDict(self, row):
    result = {}
    result['mID'] = row[0]
    result['pID'] = row[1]
    result['rType'] = row[2]
    return result

def mapToCount(self, row):
    result = {}
    result['mID'] = row[0]
    result['total'] = row[1]
    return result





