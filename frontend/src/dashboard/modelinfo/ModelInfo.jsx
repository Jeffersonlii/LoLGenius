import './ModelInfo.scss';
import * as React from 'react';

function ModelInfo() {
    return (
        <div id="mi-host">
            <div id="data-features">
                <h1>Data Features</h1>
                <p>
                    Data is collected via the Riot Games API, currently 20
                    features are used to train the model
                </p>
                <ul>
                    <li>
                        10 features for each player's MMR (collected via
                        whatismymmr API)
                    </li>
                    <li>10 features for each player's Tilt Score</li>
                    <ul>
                        <li>
                            Calculated as the weighted sum of the player's
                            performance in their last 5 games
                        </li>
                    </ul>
                </ul>
                <p>
                    {' '}
                    These features were selected on the fundemental fact that
                    the team with the better players win on average
                </p>
                <p>
                    {' '}
                    Data was collected in 16 hours and resulting in 850 total
                    data points
                </p>
            </div>
            <div id="model">
                <h1>Model</h1>
                <p>
                    The machine learning model used is a neural network with 3
                    hidden layes of size 8, with relu activation
                </p>
                <h2>Summaries</h2>
                <h3>Training Set Accuracy</h3>{' '}
                <code>
                    <pre>
                        {`
              precision    recall  f1-score   support

       False       0.81      0.74      0.77       294
        True       0.76      0.83      0.79       299

    accuracy                           0.78       593
   macro avg       0.79      0.78      0.78       593
weighted avg       0.79      0.78      0.78       593
                                
                        `}
                    </pre>
                </code>
                <h3>Validation Set Accuracy</h3>
                <code>
                    <pre>
                        {`
              precision    recall  f1-score   support

       False       0.78      0.71      0.74       131
        True       0.72      0.79      0.75       124

    accuracy                           0.75       255
   macro avg       0.75      0.75      0.75       255
weighted avg       0.75      0.75      0.75       255
                                
                        `}
                    </pre>
                </code>
            </div>
        </div>
    );
}

export default ModelInfo;
