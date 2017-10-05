import numpy as np
from lightfm import LightFM
from fetch_lastfm import fetch_lastfm


data = fetch_lastfm()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=15, num_threads=2)

# Get recommendationns function
def get_recommendations(model, coo_mtrx):

    n_items = coo_mtrx.shape[1]

    while True:
        try:
            user = raw_input('Select user (0 to %s): ' % data['users'])
            if  0<=int(user)<=int(data['users']):
                print(int(data['users']))
                print '\n' 
                # TODO create known positives
                # Artists the model predicts they will like
                scores = model.predict(user, np.arange(n_items))
                # print len(scores),n_items
                top_scores = np.argsort(-scores)[:3]

                print 'Recomendations for user %s:' % user

                for x in top_scores.tolist():
                    for movie, values in data['movies'].iteritems():
                        if int(x) == values['id']:
                            print '   - %s' % values['name']

                print '\n' # Get it pretty
            else:
                print("Invalid Input  ..")
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected")
            print("Quitting !!!")
            return




get_recommendations(model, data['matrix'])

