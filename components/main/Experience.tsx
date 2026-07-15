import React from "react";

const Experience = () => {
    return (
        <div
            className="flex flex-col items-center justify-center py-20 z-[20]"
            id="experience"
        >
            <h1 className="text-[40px] font-semibold text-transparent bg-clip-text bg-gradient-to-r from-purple-500 to-cyan-500 py-20">
                Experience
            </h1>
            <div className="h-full w-full flex flex-col items-center justify-center px-4 md:px-10">
                <div className="w-full max-w-4xl border border-[#2A0E61] bg-[#0300145e] rounded-2xl p-6 md:p-10 shadow-lg shadow-[#2A0E61]/50">
                    <h2 className="text-2xl font-bold text-white mb-2">Software Development Intern</h2>
                    <h3 className="text-xl text-transparent bg-clip-text bg-gradient-to-r from-purple-500 to-cyan-500 font-semibold mb-2">Cognifyz Technologies</h3>
                    <p className="text-gray-400 text-sm mb-6">Mar 2026 - May 2026</p>
                    
                    <p className="text-gray-200 mb-6 text-lg">
                        Gained hands-on experience across multiple domains of software engineering
                    </p>
                    
                    <ul className="list-disc list-inside text-gray-300 space-y-3">
                        <li className="leading-relaxed"><span className="font-semibold text-white">Software Development</span> — Built and maintained production-grade applications</li>
                        <li className="leading-relaxed"><span className="font-semibold text-white">Machine Learning</span> — Worked on ML models and data-driven solutions</li>
                        <li className="leading-relaxed"><span className="font-semibold text-white">Android Development</span> — Developed mobile applications for the Android platform</li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default Experience;
