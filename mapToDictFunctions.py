def mapGroupToDict(row):
    result = {}
    result['gID'] = row[0]
    result['pID'] = row[1]
    result['gName'] = row[2]
    return result


def mapMessageToDict(row):
    result = {}
    result['mID'] = row[0]
    result['mText'] = row[1]
    result['timedate'] = row[2]
    result['pID'] = row[3]
    result['gID'] = row[4]
    return result


def mapPersonToDict(row):
    result = {}
    result['pID'] = row[0]
    result['username'] = row[1]
    result['password'] = row[2]
    result['pFirstName'] = row[3]
    result['pLastName'] = row[4]
    result['pPhone'] = row[5]
    result['pEmail'] = row[6]
    return result

def mapHashTagToDict(row):
    result = {}
    result['hID'] = row[0]
    result['hText'] = row[1]
    return result

def mapToReactDict(row):
    result = {}
    result['mID'] = row[0]
    result['pID'] = row[1]
    result['rType'] = row[2]
    return result

def mapToCount(row):
    result = {}
    result['mID'] = row[0]
    result['total'] = row[1]
    return result

def mapMessageInfoToDict(row):
    result = {}
    result['pID'] = row[0]
    result['mID'] = row[1]
    result['numOfLikes'] = row[2]
    result['numOfDislikes'] = row[3]
    result['mText'] = row[4]
    result['timedate'] = row[5]
    result['username'] = row[6]
    result['pFirstName'] = row[7]
    result['pLastName'] = row[8]
    return result





