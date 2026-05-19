import React, {useMemo, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {motion} from 'framer-motion';
import {Mic, Play, Search, Sparkles, Plus, Check} from 'lucide-react';
import './styles.css';

const posters = [
  ['Neon Harbor', 'Cyber mystery', 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=900&q=80'],
  ['Signal Zero', 'AI thriller', 'https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=900&q=80'],
  ['Afterlight', 'Space drama', 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=900&q=80'],
  ['Midnight Loop', 'Time puzzle', 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=900&q=80']
];

function App() {
  const [query, setQuery] = useState('');
  const [watchlist, setWatchlist] = useState(() => JSON.parse(localStorage.getItem('watchlist') || '[]'));
  const filtered = useMemo(() => posters.filter(p => p[0].toLowerCase().includes(query.toLowerCase()) || p[1].toLowerCase().includes(query.toLowerCase())), [query]);
  const add = title => {
    const next = [...new Set([...watchlist, title])];
    setWatchlist(next);
    localStorage.setItem('watchlist', JSON.stringify(next));
  };
  return <main>
    <nav><strong>OTT Studio</strong><div><button aria-label="Voice search"><Mic size={18}/></button><button><Sparkles size={18}/> AI Theme</button></div></nav>
    <section className="hero">
      <div><h1>Cinematic AI Streaming UI</h1><p>Prompt-generated recommendations, animated previews, watchlist memory, and accessible search.</p>
      <label><Search size={18}/><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search titles or moods"/></label></div>
    </section>
    <section className="rail">{filtered.map((movie, i) => <motion.article initial={{opacity:0,y:20}} animate={{opacity:1,y:0}} transition={{delay:i*.08}} key={movie[0]}>
      <img src={movie[2]} loading="lazy" alt={`${movie[0]} poster`}/><div><h2>{movie[0]}</h2><p>{movie[1]}</p>
      <button onClick={()=>add(movie[0])}>{watchlist.includes(movie[0]) ? <Check size={18}/> : <Plus size={18}/>} Watchlist</button><button><Play size={18}/> Trailer</button></div>
    </motion.article>)}</section>
  </main>;
}

createRoot(document.getElementById('root')).render(<App/>);
