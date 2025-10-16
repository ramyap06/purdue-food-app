import React from 'react';

export default function Section({children}) {
    return (
        <li className="text-black font-sanserif text-xl hover:text-amber-300">
            <a href="#">{children}</a>
        </li>
    );
}