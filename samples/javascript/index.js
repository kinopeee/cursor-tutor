///////////////////////
// Welcome to Cursor //
///////////////////////

/*
Step 1: Try generating a react component that lets you play tictactoe with Cmd+K or Ctrl+K on a new line.
  - Then integrate it into the code below and run with npm start

Step 2: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
  - Instruct it to change the game in some way (e.g. add inline styles, add a start screen, make it 4x4 instead of 3x3)

Step 3: Hit Cmd+L or Ctrl+L and ask the chat what the code does

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
*/


import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

function Square({ value, onClick }) {
  const style = {
    height: '50px', // 高さを指定
    width: '50px',  // 幅を指定
    fontSize: '24px' // フォントサイズを大きくする
  };

  return (
    <button style={style} className="square" onClick={onClick}>
      {value}
    </button>
  );
}

function Board() {
  const [squares, setSquares] = useState(Array(16).fill(null));
  const [xIsNext, setXIsNext] = useState(true);

  function handleClick(i) {
    const squaresCopy = squares.slice();
    if (squaresCopy[i]) return;
    squaresCopy[i] = xIsNext ? 'X' : 'O';
    setSquares(squaresCopy);
    setXIsNext(!xIsNext);
  }

  function renderSquare(i) {
    return <Square value={squares[i]} onClick={() => handleClick(i)} />;
  }

  // CSSスタイルを追加して、コマ枠の表示を整える
  const boardStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
    gap: '10px'
  };

  return (
    <div style={boardStyle}>
      {Array.from({ length: 16 }, (_, i) => renderSquare(i))}
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], // 横
    [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], // 縦
    [0, 5, 10, 15], [3, 6, 9, 12]  // 斜め
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c, d] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c] && squares[a] === squares[d]) {
      return squares[a];
    }
  }
  return null;
}

function Game() {
  const [squares, setSquares] = useState(Array(16).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const winner = calculateWinner(squares);

  function handleClick(i) {
    const squaresCopy = squares.slice();
    if (squaresCopy[i] || winner) return;
    squaresCopy[i] = xIsNext ? 'X' : 'O';
    setSquares(squaresCopy);
    setXIsNext(!xIsNext);
  }

  function renderSquare(i) {
    return <Square value={squares[i]} onClick={() => handleClick(i)} />;
  }

  const boardStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
    gap: '10px'
  };

  return (
    <div className="game">
      <div className="game-board" style={boardStyle}>
        {Array.from({ length: 16 }, (_, i) => renderSquare(i))}
      </div>
      {winner && <div className="winner">勝者: {winner}</div>}
    </div>
  );
}

function App() {
  const [start, setStart] = useState(false);

  return (
    <div className="App">
      {!start ? (
        <button onClick={() => setStart(true)}>ゲームを始める</button>
      ) : (
        <Game />
      )}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
