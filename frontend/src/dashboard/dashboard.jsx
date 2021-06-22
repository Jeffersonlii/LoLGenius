import './dashboard.scss';
import { Input, SIZE } from 'baseui/input';
import * as React from 'react';
import { Button } from 'baseui/button';
import { ListItem, ListItemLabel } from 'baseui/list';
import ChevronRight from 'baseui/icon/chevron-right';
import axios from 'axios';
import { Spinner } from 'baseui/spinner';
import { Drawer, ANCHOR } from 'baseui/drawer';

import ModelInfo from './modelinfo/ModelInfo';
function Dashboard() {
    const [value, setValue] = React.useState('');
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(undefined);
    const [isDrawerOpen, setIsDrawerOpen] = React.useState(false);

    return (
        <div id="host">
            <section id="title-section">LoL Genius</section>
            <section id="input-area">
                <Input
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    size={SIZE.large}
                    placeholder="Summoner Name"
                    clearOnEscape
                    place
                />
                <Button
                    disabled={loading}
                    onClick={() => {
                        setLoading(true);
                        setResult(undefined);
                        // http://127.0.0.1:5000
                        axios
                            .get(
                                `/api/winprob-by-summoner/${
                                    value === ''
                                        ? '%20'
                                        : value.replace(/\s/g, '%20')
                                }`
                            )
                            .then((res) => {
                                setResult({ ...res.data, error: false });
                                setLoading(false);
                            })
                            .catch((error) => {
                                setResult({
                                    ...error.response.data,
                                    error: true,
                                });
                                setLoading(false);
                            });
                    }}
                >
                    Predict
                </Button>
            </section>
            <section id="result-area">
                {loading && <Spinner />}
                {result &&
                    (result.error ? (
                        <Input value={result.msg} error />
                    ) : result.win ? (
                        <Input value={'Win! 🙂'} positive />
                    ) : (
                        <Input value={'Loss 🙃'} error />
                    ))}
            </section>

            <section id="desc-area">
                Enter your League of Legends summoner name and LoLGenius predict
                the outcome of your current game! (NA Only)
                {[
                    <>
                        Powered by{' '}
                        <a
                            href="blah doesnt matter"
                            onClick={(e) => {
                                e.preventDefault();
                                setIsDrawerOpen(true);
                            }}
                        >
                            machine learning
                        </a>
                        !
                    </>,
                    '73% accurate!',
                ].map((content) => {
                    return (
                        <ListItem
                            artwork={(props) => <ChevronRight {...props} />}
                        >
                            <ListItemLabel>{content}</ListItemLabel>
                        </ListItem>
                    );
                })}
            </section>
            <footer>
                <div id="socials">
                    <a
                        href="https://jeffersonli.dev/"
                        target="_blank"
                        rel="noreferrer"
                    >
                        More
                    </a>
                    <a
                        href="https://www.linkedin.com/in/jeffersonlii/"
                        target="_blank"
                        rel="noreferrer"
                    >
                        LinkedIn
                    </a>
                    <a
                        href="https://github.com/Jeffersonlii"
                        target="_blank"
                        rel="noreferrer"
                    >
                        GitHub
                    </a>
                    <a
                        href="https://github.com/Jeffersonlii/LoLGenius"
                        target="_blank"
                        rel="noreferrer"
                    >
                        Source Code
                    </a>
                </div>
                ©{new Date().getFullYear()} Jefferson Li. All rights reserved.
            </footer>
            <Drawer
                isOpen={isDrawerOpen}
                autoFocus
                onClose={() => setIsDrawerOpen(false)}
                anchor={ANCHOR.bottom}
                showBackdrop={false}
                size={'auto'}
            >
                <ModelInfo></ModelInfo>
            </Drawer>
        </div>
    );
}

export default Dashboard;
