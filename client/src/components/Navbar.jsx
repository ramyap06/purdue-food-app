import React from "react";
import Section from "./Section";

export default function Navbar() {
    return (
        <header className="bg-amber-200">
            <nav className="">
                <ul className="flex items-center gap-20 p-4">
                    <Section>Home</Section>
                    <Section>Halls</Section>
                    <Section>About</Section>
                    <Section>FAQ</Section>
                </ul>
            </nav>
        </header>
    );
}