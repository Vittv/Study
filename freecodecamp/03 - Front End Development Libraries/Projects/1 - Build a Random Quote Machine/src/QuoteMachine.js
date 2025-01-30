import React, { useState, useEffect} from 'react';
import { Button, Container, Row, Col } from 'react-bootstrap';

const QuoteMachine = () => {
    const [quote, setQuote] = useState('');
    const [author, setAuthor] = useState('');

    const fetchQuote = async () => {
        const response = await fetch('https://api.quotable.io/random')
        const data = await response.json();
        setQuote(data.content);
        setAuthor(data.author);
    };


    useEffect(() => {
        fetchQuote();
    }, []);

    return (
        <Container className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
            <Row>
                <Col>
                    <div className="quote-box p-4 rounded shadow">
                        <h2>{quote}</h2>
                        <p className="text-end">- {author}</p>
                        <Button variant="primary" onClick={fetchQuote}>New quote</Button>
                    </div>
                </Col>
            </Row>
        </Container>
    );
};

export default QuoteMachine;