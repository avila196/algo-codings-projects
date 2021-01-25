#!/usr/bin/env python3


class SocialNetwork:

    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        self.users = {}

    def list_users(self):
        '''List all users in the network

        Returns:
            [str]: A list of usernames
        '''
        #The list of usernames is given as all keys of the dictionary
        return list(self.users.keys())

    def add_user(self, user):
        '''Add a user to the network

        This user will have no friends initially.

        Arguments:
            user (str): The username of the new user

        Returns:
            None
        '''
        #We add the current user to the dictionary with an empty list as its
        #value
        self.users[user] = []

    def add_friend(self, user, friend):
        '''Adds a friend to a user

        Note that "friends" are one-directional - this is the equivalent of
        "following" someone.

        If either the user or the friend is not a user in the network, they
        should be added to the network.

        Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed

        Returns:
            None
        '''
        #First, we check if the user or the friend are not in the network
        #already. If one of them is not there, we add it
        if user not in self.users:
            self.add_user(user)
        if friend not in self.users:
            self.add_user(friend)
        #Finally, we add the current relation between the user and the friend
        #it follows. We append the friend to the user list of friends
        self.users[user].append(friend)

    def get_friends(self, user):
        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        #We just return the List of friends of the given user
        return self.users[user]

    def suggest_friend(self, user):
        '''Suggest a friend to the user

        See project specifications for details on this algorithm.

        Arguments:
            user (str): The username of the user to find a friend for

        Returns:
            str: The username of a new candidate friend for the user
        '''
        #First of all, we need to find the most-similar user to the current
        #user. To do that, we loop through all users. Also, using the same
        #loop, we can create a dictionary that holds all the users as keys
        #and the number of users that follow them (friends) as the keys
        most_similar = None
        jaccard_index = 0
        followers = {}
        for other_user in self.users:
            if other_user != user:
                #For the current user, we first find the friends that both follow
                #and we also create a Set for all the friends they have
                all_friends = set(self.users[user])
                both = 0
                for friend in self.users[other_user]:
                    #First, we add the friend to the set of friends (union)
                    all_friends.add(friend)
                    #Now, if both follow it, we count it
                    if friend in self.users[user]:
                        both += 1
                    #Also, we increase 1 for the number of followers of the friend
                    if friend not in followers:
                        followers[friend] = 1
                    else:
                        followers[friend] += 1
                #Now, we calculate the Jaccard Index for these two friends
                index = both / (len(all_friends))
                #If the current index is greater than the one so far, we change it
                if index > jaccard_index:
                    most_similar = other_user
                    jaccard_index = index
        #Now, using the most similar user, we return the friend with the greatest
        #number of followers that is not friend (followed) from the user
        recommendation = None
        max_num = 0
        #We loop through the friends of the most similar
        for friend in self.users[most_similar]:
            #If not friend of user and greater than the one with max followers, we change it
            if friend not in self.users[user] and followers[friend] > max_num:
                recommendation = friend
                max_num = followers[friend]
        #Finally, we return the recommendation
        return recommendation
            
    
    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file

    Arguments:
        filename (str): The name of the network file

    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network


def main():
    network = create_network_from_file('simple.network')
    print(network.to_dot())
    print(network.suggest_friend('francis'))


if __name__ == '__main__':
    main()