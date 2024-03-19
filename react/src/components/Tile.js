import React from 'react'
import './Tile.css';

function Tile(props) {
    const className = ['tile', props.flag % 2 === 0 && 'tile-black', 
            props.flag % 2 !== 0 && 'tile-white', 
            props.highlight && 'tile-highlight'].filter(Boolean).join(' ');
    return(
        <div className = {className}>
            {props.image && <div className = 'chessPiece' style={{backgroundImage: `url(${props.image})`}}></div>}
            {/* <img src = {props.image} className="chess-piece-image"></img> */}
        </div>
    )
}
export default Tile
