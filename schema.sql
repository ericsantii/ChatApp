
create table Person(pID serial primary key, username varchar(8) UNIQUE, passwd chkpass, uFirstName varchar(100), uLastName varchar(100), pPhone varchar(15), pEmail varchar(50));

create table ChatGroup(gID serial primary key, gName varchar(100), gOwner integer references Person(pID));

create table Message(mID serial primary key, mText varchar(1000), timedate timestamp, multimedia bytea, posterID integer references Person(pID), groupID integer references ChatGroup(gID));

create table react(mID integer references Message(mID), pID integer references Person(pID), rType boolean, primary key(mID, pID));

create table hasContact(userID integer references Person(pID), contactedID integer references Person(pID), primary key(userID, contactedID));

create table isMember(userID integer references Person(pID), groupID integer references ChatGroup(gID), primary key(userID, groupID));

create table reply(originalMessageID integer references Message(mID), replyMessageID integer references Message(mID), primary key(originalMessageID, replyMessageID));
