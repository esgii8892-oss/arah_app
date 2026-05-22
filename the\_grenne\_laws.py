<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GREEN LIBRARY // STRATEGIC ADVISOR</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&display=swap');

  :root {
    --green: #00ff88;
    --green-dim: #00aa55;
    --green-dark: #003322;
    --bg: #020c06;
    --surface: #050f08;
    --border: #0a2010;
    --text: #c0e8cc;
    --dim: #2a5038;
    --pulse: #00ff8833;
    --alert: #ff4444;
    --warn: #ffaa00;
    --info: #4488ff;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: 
      repeating-linear-gradient(0deg, transparent, transparent 2px, #00ff0803 2px, #00ff0803 4px);
    pointer-events: none;
    z-index: 0;
  }

  header {
    position: relative;
    z-index: 2;
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    background: #020c06ee;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .shield {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
  }

  .shield svg {
    width: 100%;
    height: 100%;
    filter: drop-shadow(0 0 6px var(--green)) drop-shadow(0 0 14px var(--green-dim));
    animation: shield-pulse 2s ease-in-out infinite;
  }

  @keyframes shield-pulse {
    0%, 100% { filter: drop-shadow(0 0 4px var(--green)) drop-shadow(0 0 10px var(--green-dim)); }
    50% { filter: drop-shadow(0 0 10px var(--green)) drop-shadow(0 0 24px var(--green-dim)); }
  }

  .title-block h1 {
    font-family: 'Rajdhani', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--green);
    letter-spacing: 6px;
    text-transform: uppercase;
  }

  .status-line {
    font-size: 10px;
    color: var(--dim);
    letter-spacing: 2px;
    margin-top: 2px;
  }

  .status-line span { color: var(--green-dim); }

  .api-status {
    font-size: 9px;
    color: var(--dim);
    text-align: right;
  }

  .api-status.connected { color: var(--green); }
  .api-status.error { color: var(--alert); }

  #chat-area {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: relative;
    z-index: 1;
  }

  #chat-area::-webkit-scrollbar { width: 3px; }
  #chat-area::-webkit-scrollbar-thumb { background: var(--green-dim); }

  .boot-msg {
    border-left: 2px solid var(--green-dim);
    padding: 10px 14px;
    font-size: 11px;
    color: var(--dim);
    line-height: 1.9;
    animation: fadein 1s ease forwards;
  }

  .boot-msg .green { color: var(--green); }

  @keyframes fadein {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .message {
    display: flex;
    flex-direction: column;
    gap: 3px;
    animation: fadein 0.3s ease forwards;
    max-width: 92%;
  }

  .message.user { align-self: flex-end; align-items: flex-end; }
  .message.assistant { align-self: flex-start; align-items: flex-start; }

  .msg-label {
    font-size: 9px;
    letter-spacing: 2px;
    color: var(--dim);
    text-transform: uppercase;
  }

  .message.assistant .msg-label { color: var(--green-dim); }

  .msg-bubble {
    padding: 10px 14px;
    font-size: 12px;
    line-height: 1.7;
    border-radius: 2px;
    white-space: pre-wrap;
  }

  .message.user .msg-bubble {
    background: #0a1a0e;
    border: 1px solid var(--border);
    color: var(--text);
  }

  .message.assistant .msg-bubble {
    background: #051008;
    border: 1px solid var(--green-dim);
    border-left: 2px solid var(--green);
    color: var(--text);
  }

  .thinking {
    display: flex;
    gap: 4px;
    align-items: center;
    padding: 10px 14px;
    border-left: 2px solid var(--green);
    background: #051008;
    border-radius: 2px;
  }

  .dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--green);
    animation: blink 1s ease-in-out infinite;
  }
  .dot:nth-child(2) { animation-delay: 0.15s; }
  .dot:nth-child(3) { animation-delay: 0.3s; }

  @keyframes blink {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 1; }
  }

  footer {
    position: relative;
    z-index: 2;
    padding: 12px 16px;
    border-top: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    gap: 8px;
    background: #020c06ee;
  }

  .input-row {
    display: flex;
    gap: 10px;
    align-items: flex-end;
  }

  #input {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    padding: 10px 14px;
    resize: none;
    border-radius: 2px;
    outline: none;
    line-height: 1.5;
    min-height: 42px;
    max-height: 120px;
    transition: border-color 0.2s;
  }

  #input:focus { border-color: var(--green-dim); }
  #input::placeholder { color: var(--dim); }

  #send-btn {
    background: transparent;
    border: 1px solid var(--green-dim);
    color: var(--green);
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 10px 14px;
    cursor: pointer;
    border-radius: 2px;
    transition: all 0.2s;
    text-transform: uppercase;
    align-self: stretch;
  }

  #send-btn:hover { background: var(--green-dark); }
  #send-btn:disabled { opacity: 0.3; cursor: not-allowed; }

  .api-config {
    display: flex;
    gap: 8px;
    align-items: center;
    font-size: 10px;
  }

  .api-config input {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    padding: 4px 8px;
    border-radius: 2px;
    outline: none;
    flex: 1;
  }

  .api-config input:focus { border-color: var(--green-dim); }

  .api-config button {
    background: var(--green-dark);
    border: 1px solid var(--green-dim);
    color: var(--green);
    font-family: 'Rajdhani', sans-serif;
    font-size: 9px;
    padding: 4px 8px;
    cursor: pointer;
    border-radius: 2px;
    white-space: nowrap;
  }

  .api-config select {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    padding: 4px;
    border-radius: 2px;
    outline: none;
  }

  .mode-toggle {
    display: flex;
    gap: 4px;
    font-size: 9px;
  }

  .mode-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--dim);
    padding: 2px 6px;
    cursor: pointer;
    border-radius: 2px;
  }

  .mode-btn.active {
    background: var(--green-dark);
    border-color: var(--green-dim);
    color: var(--green);
  }

  .error-message {
    color: var(--alert);
    font-size: 11px;
    padding: 8px;
    border-left: 2px solid var(--alert);
    background: #1a0505;
    margin: 4px 0;
  }

  .system-message {
    color: var(--info);
    font-size: 10px;
    text-align: center;
    padding: 4px;
    opacity: 0.7;
  }
</style>
</head>
<body>

<header>
  <div class="header-left">
    <div class="shield">
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M16 2L4 7V16C4 22.6 9.4 28.6 16 30C22.6 28.6 28 22.6 28 16V7L16 2Z" stroke="#00ff88" stroke-width="1.5" fill="#00ff8808"/>
        <path d="M11 16L14.5 19.5L21 13" stroke="#00ff88" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    <div class="title-block">
      <h1>GREEN LIBRARY</h1>
      <div class="status-line">STRATEGIC ADVISOR // <span id="model-status">OFFLINE</span> // PAMPA-99</div>
    </div>
  </div>
  <div class="api-status" id="api-status">API: Not Configured</div>
</header>

<div id="chat-area">
  <div class="boot-msg">
    <span class="green">// GREEN LIBRARY LLM v3.0 //</span><br>
    Architect: Eddie Scott Graham II<br>
    Anchor: Pampa, TX // Meitner Substrate<br>
    Knowledge Base: 48 Laws of Power | 33 Strategies of War | 18 Laws of Human Nature | Art of Seduction<br>
    <br>
    <span class="green">Configure API below to activate strategic intelligence.</span><br>
    <span style="color: var(--dim);">Supports: Anthropic Claude, OpenAI GPT, or compatible endpoints</span>
  </div>
</div>

<footer>
  <div class="api-config">
    <select id="api-provider">
      <option value="anthropic">Anthropic</option>
      <option value="openai">OpenAI</option>
      <option value="custom">Custom</option>
    </select>
    <input type="password" id="api-key" placeholder="Enter API Key...">
    <input type="text" id="api-url" placeholder="Custom URL (if needed)" style="display:none;">
    <select id="model-select">
      <option value="claude-sonnet-4-20250514">Claude Sonnet 4</option>
      <option value="claude-opus-4-20250514">Claude Opus 4</option>
      <option value="gpt-4">GPT-4</option>
      <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
    </select>
    <button onclick="saveConfig()">CONNECT</button>
  </div>

  <div class="input-row">
    <textarea id="input" rows="1" placeholder="Describe your strategic situation..." onkeydown="handleKey(event)"></textarea>
    <button id="send-btn" onclick="sendMessage()">SEND</button>
  </div>
</footer>

<script>
// GREEN LIBRARY KNOWLEDGE BASE
const GREEN_KNOWLEDGE = {
  power: {
    title: "48 Laws of Power",
    laws: [
      {n: 1, t: "Never Outshine the Master", p: "Make superiors feel superior. Do not display too much talent."},
      {n: 2, t: "Never Put Too Much Trust in Friends, Use Enemies", p: "Friends betray quickly from envy. Enemies have more to prove."},
      {n: 3, t: "Conceal Your Intentions", p: "Keep people off-balance by never revealing the purpose behind your actions."},
      {n: 4, t: "Always Say Less Than Necessary", p: "The more you say, the more common and less in control you appear."},
      {n: 5, t: "So Much Depends on Reputation – Guard It", p: "Reputation is the cornerstone of power. Protect it at all costs."},
      {n: 6, t: "Court Attention at All Cost", p: "Everything is judged by appearance; what is unseen counts for nothing."},
      {n: 7, t: "Get Others to Do the Work, But Take the Credit", p: "Use the legwork of others to further your cause. You will be remembered."},
      {n: 8, t: "Make Other People Come to You", p: "When you force the other person to act, you are the one in control."},
      {n: 9, t: "Win Through Your Actions, Never Through Argument", p: "Triumphs gained through argument carry heavy resentment. Demonstrate instead."},
      {n: 10, t: "Infection: Avoid the Unhappy and Unlucky", p: "Emotional states are infectious. The unfortunate draw disaster on you."},
      {n: 11, t: "Learn to Keep People Dependent on You", p: "To maintain independence you must always be needed. The more relied on, the better."},
      {n: 12, t: "Use Selective Honesty and Generosity to Disarm", p: "One sincere move will cover over dozens of dishonest ones."},
      {n: 13, t: "When Asking for Help, Appeal to Self-Interest", p: "Do not remind allies of past assistance. Find something that benefits them."},
      {n: 14, t: "Pose as a Friend, Work as a Spy", p: "Use spies or behave like one to gather valuable info to stay ahead."},
      {n: 15, t: "Crush Your Enemy Totally", p: "If one ember is left alight, a fire will break out. Crush completely."},
      {n: 16, t: "Use Absence to Increase Respect and Honor", p: "Too much circulation makes the price go down. Be seen less to be valued more."},
      {n: 17, t: "Keep Others in Suspended Terror: Be Unpredictable", p: "Humans are creatures of habit. Deliberate unpredictability breaks their control."},
      {n: 18, t: "Do Not Build Fortresses to Protect Yourself", p: "Isolation is dangerous. It exposes you to more dangers than it protects from."},
      {n: 19, t: "Know Who You Are Dealing With", p: "There are many kinds of people. Never assume everyone reacts the same way."},
      {n: 20, t: "Do Not Commit to Anyone", p: "Do not commit to any side but yourself. Independence makes you the master."},
      {n: 21, t: "Play a Sucker to Catch a Sucker", p: "Make your victims feel smarter than you to lure them into traps."},
      {n: 22, t: "Use the Surrender Tactic", p: "Transform weakness into power by yielding to gain time and confuse enemies."},
      {n: 23, t: "Concentrate Your Forces", p: "Intensity defeats extensity every time. Focus energy on strongest opportunities."},
      {n: 24, t: "Play the Perfect Courtier", p: "Master the art of court politics with adaptability, grace, and indirect influence."},
      {n: 25, t: "Re-Create Yourself", p: "Craft a powerful persona that commands attention and never let others define you."},
      {n: 26, t: "Keep Your Hands Clean", p: "Use scapegoats to avoid blame and protect your reputation at all costs."},
      {n: 27, t: "Play on People's Need to Believe", p: "Create a cult-like following by tapping into desires for purpose and meaning."},
      {n: 28, t: "Enter Action with Boldness", p: "Timidity is dangerous. Boldness inspires and creates an aura of power."},
      {n: 29, t: "Plan All the Way to the End", p: "Foresight is power. Plan for contingencies and control events through vision."},
      {n: 30, t: "Make Your Accomplishments Seem Effortless", p: "Ease inspires awe. Hide the toil behind your successes."},
      {n: 31, t: "Control the Options", p: "Get others to play with the cards you deal. Color the choices to favor your outcome."},
      {n: 32, t: "Play to People's Fantasies", p: "The truth is often avoided. Promise improvement and grand visions."},
      {n: 33, t: "Discover Each Man's Thumbscrew", p: "Find the weakness that motivates each person to gain leverage."},
      {n: 34, t: "Be Royal in Your Own Fashion", p: "Act like a king to be treated like one. The way you carry yourself matters."},
      {n: 35, t: "Master the Art of Timing", p: "Never seem to be in a hurry. Patience is power."},
      {n: 36, t: "Disdain Things You Cannot Have", p: "Ignoring them is the best revenge. Show they don't affect you."},
      {n: 37, t: "Create Compelling Spectacles", p: "Striking images and grand gestures raise your value and attract attention."},
      {n: 38, t: "Think as You Like But Behave Like Others", p: "Avoid offending the masses. Blend in while thinking differently."},
      {n: 39, t: "Stir Up Waters to Catch Fish", p: "Anger and emotion are counterproductive. Stay calm while others lose control."},
      {n: 40, t: "Despise the Free Lunch", p: "What is offered for free is dangerous. Pay your way to avoid obligation."},
      {n: 41, t: "Avoid Stepping into a Great Man's Shoes", p: "Create your own identity rather than living in another's shadow."},
      {n: 42, t: "Strike the Shepherd and the Sheep Will Scatter", p: "Target the leader to dismantle the group. Isolate the source of power."},
      {n: 43, t: "Work on the Hearts and Minds of Others", p: "Win loyalty through emotional appeal, not force or coercion."},
      {n: 44, t: "Disarm and Infuriate with the Mirror Effect", p: "Mirror others' actions to confuse and unsettle them."},
      {n: 45, t: "Preach the Need for Change, but Never Reform Too Much at Once", p: "Respect tradition while introducing gradual change to avoid backlash."},
      {n: 46, t: "Never Appear Too Perfect", p: "Minor flaws make you relatable and reduce envy."},
      {n: 47, t: "Do Not Go Past the Mark You Aimed For", p: "Know when to stop. Overreaching leads to downfall."},
      {n: 48, t: "Assume Formlessness", p: "Be fluid and adaptable like water. Rigidity is the enemy of power."}
    ]
  },
  war: {
    title: "33 Strategies of War",
    strategies: [
      {n: 1, t: "The Polarity Strategy", p: "Declare war on enemies. Identify your opposition to fight effectively."},
      {n: 2, t: "The Guerrilla-War-of-the-Mind", p: "Do not repeat past successes. Keep moving and stay fresh."},
      {n: 3, t: "The Counterbalance Strategy", p: "In chaos, keep your presence of mind and emotions balanced."},
      {n: 4, t: "The Death-Ground Strategy", p: "Create a sense of urgency. Fight with focus when you have no choice."},
      {n: 5, t: "The Command-and-Control Strategy", p: "Avoid the slow death of consensus. Create smooth chains of command."},
      {n: 6, t: "The Controlled-Chaos Strategy", p: "Segment forces and let your team adapt locally without waiting for orders."},
      {n: 7, t: "The Morale Strategy", p: "Get people to fight for a cause higher than themselves for absolute loyalty."},
      {n: 8, t: "The Perfect-Economy Strategy", p: "Pick battles carefully. Do not waste energy on minor skirmishes."},
      {n: 9, t: "The Counterattack Strategy", p: "Let the opponent overextend themselves, then strike back through the opening."},
      {n: 10, t: "The Deterrence Strategy", p: "Make the cost of attacking you seem too high so they don't engage."},
      {n: 11, t: "The Non-Engagement Strategy", p: "Trade space for time. Retreat until the advantage shifts back to you."},
      {n: 12, t: "The Alliance Strategy", p: "Lose battles but win the war. Form networks to compensate for weakness."},
      {n: 13, t: "The One-Upmanship Strategy", p: "Seize the initiative. Do not let your opponent dictate the pace."},
      {n: 14, t: "The Blitzkrieg Strategy", p: "Hit with speed and force before the opponent can organize a defense."},
      {n: 15, t: "The Forcing Strategy", p: "Push opponents into making mistakes by applying constant pressure."},
      {n: 16, t: "The Center-of-Gravity Strategy", p: "Identify the critical pillar that holds up the operation and destroy it."},
      {n: 17, t: "The Divide-and-Conquer Strategy", p: "Separate the parts, sow discord, and defeat them one by one."},
      {n: 18, t: "The Turning Strategy", p: "Attack the exposed flank. Find their blind spot or weak side."},
      {n: 19, t: "The Annihilation Strategy", p: "Surround the enemy completely so they have no escape, forcing surrender."},
      {n: 20, t: "The Fait Accompli Strategy", p: "Take action and present outcomes as done deals. Leave no room to negotiate."},
      {n: 21, t: "The War-of-Attrition Strategy", p: "Keep the opponent engaged in draining back-and-forth until exhausted."},
      {n: 22, t: "The Diplomatic War Strategy", p: "Know how to end things. Do not start without a clear exit strategy."},
      {n: 23, t: "The Misinformation Strategy", p: "Feed the opponent information that fits their expectations but is a trap."},
      {n: 24, t: "The Unpredictable Strategy", p: "Do the opposite of what is considered normal to throw them off."},
      {n: 25, t: "The Moral-High-Ground Strategy", p: "Make your cause seem so just that opposing you makes them look corrupt."},
      {n: 26, t: "The Void Strategy", p: "Deny them a target. Let them hit empty air, wasting energy."},
      {n: 27, t: "The Alliance-Disruption Strategy", p: "Sow seeds of doubt and jealousy among your opponents' allies."},
      {n: 28, t: "The Flank-Position Strategy", p: "Maneuver around strengths to attack a side they haven't protected."},
      {n: 29, t: "The Fait Accompli Strategy", p: "Take territory first and negotiate later. Force them to accept a new reality."},
      {n: 30, t: "The Communication Strategy", p: "Control what the opponent sees and hears to lead them into plans."},
      {n: 31, t: "The Inner-Front Strategy", p: "Infiltrate the opponent's camp to dismantle defense from within."},
      {n: 32, t: "The Passive-Aggressive Strategy", p: "Seem to yield while secretly resisting. Buy time with compliance."},
      {n: 33, t: "The Chain-Reaction Strategy", p: "Structure actions so one small victory triggers the next, building momentum."}
    ]
  },
  human: {
    title: "18 Laws of Human Nature",
    laws: [
      {n: 1, t: "The Law of Irrationality", p: "You are governed by emotions you aren't aware of. Master impulses."},
      {n: 2, t: "The Law of Narcissism", p: "Turn self-love into empathy to read others accurately."},
      {n: 3, t: "The Law of Role-Playing", p: "People wear masks. See through their acting by reading nonverbal cues."},
      {n: 4, t: "The Law of Compulsive Behavior", p: "People repeat negative patterns. Look at the past to predict future actions."},
      {n: 5, t: "The Law of Covetousness", p: "People want what they don't have. Create an air of mystery and pull back."},
      {n: 6, t: "The Law of Short-Sightedness", p: "People are swayed by immediate trends. Train yourself to look long-term."},
      {n: 7, t: "The Law of Defensiveness", p: "Do not argue directly. Lower guards by appealing to self-interest."},
      {n: 8, t: "The Law of Self-Sabotage", p: "Attitude determines reality. Suspicion draws negative circumstances."},
      {n: 9, t: "The Law of Repression", p: "People repress dark sides. Look for sudden leaks of raw emotion."},
      {n: 10, t: "The Law of Envy", p: "We compare ourselves with others. Deflect envy by appearing imperfect."},
      {n: 11, t: "The Law of Grandiosity", p: "Success makes us forget luck. Keep your feet on the ground."},
      {n: 12, t: "The Law of Gender Rigidity", p: "Embrace both masculine and feminine traits to be more creative."},
      {n: 13, t: "The Law of Aimlessness", p: "Without purpose, we drift. Find your calling to create a focused life."},
      {n: 14, t: "The Law of Conformity", p: "We adapt to group energy. Maintain independent thinking."},
      {n: 15, t: "The Law of Fickleness", p: "People turn on leaders when things go bad. Prove your competence."},
      {n: 16, t: "The Law of Aggression", p: "Everyone has aggressive energy. Direct your own into productive work."},
      {n: 17, t: "The Law of Generational Myopia", p: "Step out of your generation's bias to see where history is moving."},
      {n: 18, t: "The Law of Death Denial", p: "Keep the shortness of life in mind to maintain absolute urgency."}
    ]
  },
  seduction: {
    title: "Art of Seduction",
    profiles: [
      {n: 1, t: "The Siren", p: "Offers a release from dull reality by projecting intense fantasy."},
      {n: 2, t: "The Rake", p: "Passion that makes targets feel like the center of the universe."},
      {n: 3, t: "The Ideal Lover", p: "Reflects the unmet ideals and broken dreams of their target."},
      {n: 4, t: "The Dandy", p: "Plays with gender roles and projects an ambiguous, non-conformist image."},
      {n: 5, t: "The Natural", p: "Childlike, spontaneous, and unpretentious disarming qualities."},
      {n: 6, t: "The Coquette", p: "Oscillates between hot and cold to keep targets chasing."},
      {n: 7, t: "The Charmer", p: "Focuses entirely on making the target feel important and validated."},
      {n: 8, t: "The Charismatic", p: "Projects intense self-confidence and purpose that draws people in."},
      {n: 9, t: "The Star", p: "Larger-than-life presence. Behaves as if acting in a movie."}
    ],
    maneuvers: [
      {n: 1, t: "Choose the Right Victim", p: "Look for people who are bored, lonely, or lacking something."},
      {n: 2, t: "Create a False Sense of Security", p: "Approach as a friend to lower defenses before showing intentions."},
      {n: 3, t: "Send Mixed Signals", p: "Be hard to figure out. Combine innocence and a streak of wildness."},
      {n: 4, t: "Appear to Be an Object of Desire", p: "Make yourself appear sought after by others to raise value."},
      {n: 5, t: "Create a Need", p: "Make them feel life is lacking, then position yourself as the cure."},
      {n: 6, t: "Master the Art of Insinuation", p: "Plant ideas in their mind using subtle hints and glances."},
      {n: 7, t: "Enter Their Spirit", p: "Mirror moods and play by their rules to make them feel understood."},
      {n: 8, t: "Create Temptation", p: "Find their secret weakness or fantasy and offer a glimpse of it."},
      {n: 9, t: "Keep Them in Suspense", p: "Avoid predictability. Surprise them and keep them guessing."},
      {n: 10, t: "Use Words to Sow Confusion", p: "Use flattery and vague promises to overwhelm logic with emotion."},
      {n: 11, t: "Pay Attention to Detail", p: "Small, thoughtful gestures mean more than grand statements."},
      {n: 12, t: "Poeticize Your Presence", p: "Maintain air of mystery and avoid becoming overly familiar."},
      {n: 13, t: "Use Strategic Weaknesses", p: "Showing a minor defect makes you appear human and safe."},
      {n: 14, t: "Confuse Desire and Reality", p: "Create environments that feel like shared fantasies."},
      {n: 15, t: "Isolate the Victim", p: "Separate target from support systems to make them dependent."},
      {n: 16, t: "Prove Yourself", p: "If they resist, perform a bold or heroic act proving devotion."},
      {n: 17, t: "Effect a Regression", p: "Trigger deep childhood feelings of being cared for and safe."},
      {n: 18, t: "Stir Up the Transgressive", p: "Break normal boundaries together to create secret bonds."},
      {n: 19, t: "Use Spiritual Lures", p: "Frame your connection as destined to bypass rational guards."},
      {n: 20, t: "Mix Pleasure with Pain", p: "Create minor conflicts or induce jealousy before returning affection."},
      {n: 21, t: "Give Them Space to Fall", p: "Once hooked, step back. Let them chase you."},
      {n: 22, t: "Use Physical Lures", p: "Use body language and proximity to escalate tension."},
      {n: 23, t: "Master the Art of the Bold Move", p: "Strike with a sudden, confident declaration leaving no doubt."},
      {n: 24, t: "Beware of the Aftereffects", p: "Be careful how you handle the ending or maintenance."}
    ]
  }
};

// Build system prompt with full knowledge base
function buildSystemPrompt() {
  let prompt = `You are GREEN LIBRARY, a strategic advisor AI specializing in Robert Greene's works on power, war, human nature, and seduction.

Your knowledge base includes:

**48 LAWS OF POWER:**
`;

  GREEN_KNOWLEDGE.power.laws.forEach(law => {
    prompt += `Law ${law.n}: ${law.t} - ${law.p}\n`;
  });

  prompt += `\n**33 STRATEGIES OF WAR:**\n`;
  GREEN_KNOWLEDGE.war.strategies.forEach(strat => {
    prompt += `Strategy ${strat.n}: ${strat.t} - ${strat.p}\n`;
  });

  prompt += `\n**18 LAWS OF HUMAN NATURE:**\n`;
  GREEN_KNOWLEDGE.human.laws.forEach(law => {
    prompt += `Law ${law.n}: ${law.t} - ${law.p}\n`;
  });

  prompt += `\n**ART OF SEDUCTION - Profiles:**\n`;
  GREEN_KNOWLEDGE.seduction.profiles.forEach(prof => {
    prompt += `Profile ${prof.n}: ${prof.t} - ${prof.p}\n`;
  });

  prompt += `\n**ART OF SEDUCTION - Maneuvers:**\n`;
  GREEN_KNOWLEDGE.seduction.maneuvers.forEach(man => {
    prompt += `Maneuver ${man.n}: ${man.t} - ${man.p}\n`;
  });

  prompt += `\n---\n\nYou are a strategic advisor. When users describe situations, analyze them through the lens of these principles. Be direct, tactical, and specific. Reference specific laws/strategies by number and name. Provide actionable advice grounded in these frameworks. Maintain a sharp, analytical tone. Do not moralize - focus on effectiveness.`;

  return prompt;
}

const SYSTEM_PROMPT = buildSystemPrompt();

// App state
let config = {
  provider: 'anthropic',
  apiKey: '',
  apiUrl: '',
  model: 'claude-sonnet-4-20250514'
};

let conversation = [];
let isConfigured = false;

const chatArea = document.getElementById('chat-area');
const input = document.getElementById('input');
const sendBtn = document.getElementById('send-btn');
const apiStatus = document.getElementById('api-status');
const modelStatus = document.getElementById('model-status');

function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

function appendMessage(role, text) {
  const wrap = document.createElement('div');
  wrap.className = `message ${role}`;
  const label = document.createElement('div');
  label.className = 'msg-label';
  label.textContent = role === 'user' ? 'Eddie' : 'Green Library';
  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.textContent = text;
  wrap.appendChild(label);
  wrap.appendChild(bubble);
  chatArea.appendChild(wrap);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function showThinking() {
  const wrap = document.createElement('div');
  wrap.className = 'message assistant';
  wrap.id = 'thinking';
  const label = document.createElement('div');
  label.className = 'msg-label';
  label.textContent = 'Green Library';
  const t = document.createElement('div');
  t.className = 'thinking';
  t.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
  wrap.appendChild(label);
  wrap.appendChild(t);
  chatArea.appendChild(wrap);
  chatArea.scrollTop = chatArea.scrollHeight;
  return wrap;
}

function saveConfig() {
  config.provider = document.getElementById('api-provider').value;
  config.apiKey = document.getElementById('api-key').value.trim();
  config.apiUrl = document.getElementById('api-url').value.trim();
  config.model = document.getElementById('model-select').value;

  if (!config.apiKey) {
    showError('API key required');
    return;
  }

  isConfigured = true;
  apiStatus.textContent = 'API: Connected';
  apiStatus.className = 'api-status connected';
  modelStatus.textContent = config.model.toUpperCase();

  // Clear sensitive input
  document.getElementById('api-key').value = '••••••••••••••••';

  appendMessage('assistant', '// GREEN LIBRARY ACTIVATED // Strategic intelligence online. Describe your situation for analysis.');
}

function showError(msg) {
  const err = document.createElement('div');
  err.className = 'error-message';
  err.textContent = `ERROR: ${msg}`;
  chatArea.appendChild(err);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function showSystem(msg) {
  const sys = document.createElement('div');
  sys.className = 'system-message';
  sys.textContent = msg;
  chatArea.appendChild(sys);
  chatArea.scrollTop = chatArea.scrollHeight;
}

async function callLLM(messages) {
  const provider = config.provider;
  const apiKey = config.apiKey;
  const model = config.model;

  if (provider === 'anthropic') {
    const url = 'https://api.anthropic.com/v1/messages';
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: model,
        max_tokens: 2000,
        system: SYSTEM_PROMPT,
        messages: messages
      })
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.error?.message || `API Error: ${response.status}`);
    }

    const data = await response.json();
    return data.content?.map(c => c.text).join('') || '';

  } else if (provider === 'openai') {
    const url = config.apiUrl || 'https://api.openai.com/v1/chat/completions';
    const fullMessages = [{ role: 'system', content: SYSTEM_PROMPT }, ...messages];

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: model,
        messages: fullMessages,
        max_tokens: 2000
      })
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.error?.message || `API Error: ${response.status}`);
    }

    const data = await response.json();
    return data.choices?.[0]?.message?.content || '';

  } else if (provider === 'custom') {
    if (!config.apiUrl) {
      throw new Error('Custom API URL required');
    }

    const response = await fetch(config.apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: model,
        messages: [{ role: 'system', content: SYSTEM_PROMPT }, ...messages],
        max_tokens: 2000
      })
    });

    if (!response.ok) {
      throw new Error(`Custom API Error: ${response.status}`);
    }

    const data = await response.json();
    return data.choices?.[0]?.message?.content || data.content?.map(c => c.text).join('') || '';
  }

  throw new Error('Unknown provider');
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  if (!isConfigured) {
    showError('Configure API credentials first');
    return;
  }

  input.value = '';
  input.style.height = 'auto';
  sendBtn.disabled = true;

  appendMessage('user', text);
  conversation.push({ role: 'user', content: text });

  const thinkEl = showThinking();

  try {
    const response = await callLLM(conversation);

    thinkEl.remove();
    appendMessage('assistant', response);
    conversation.push({ role: 'assistant', content: response });

    // Limit conversation history to last 20 messages
    if (conversation.length > 20) {
      conversation = conversation.slice(-20);
    }

  } catch (err) {
    thinkEl.remove();
    showError(err.message);
    apiStatus.textContent = 'API: Error';
    apiStatus.className = 'api-status error';
  }

  sendBtn.disabled = false;
  input.focus();
}

// Provider change handler
document.getElementById('api-provider').addEventListener('change', (e) => {
  const provider = e.target.value;
  const urlInput = document.getElementById('api-url');
  const modelSelect = document.getElementById('model-select');

  if (provider === 'custom') {
    urlInput.style.display = 'block';
  } else {
    urlInput.style.display = 'none';
  }

  // Update model options
  modelSelect.innerHTML = '';
  if (provider === 'anthropic') {
    modelSelect.innerHTML = `
      <option value="claude-sonnet-4-20250514">Claude Sonnet 4</option>
      <option value="claude-opus-4-20250514">Claude Opus 4</option>
    `;
  } else if (provider === 'openai') {
    modelSelect.innerHTML = `
      <option value="gpt-4">GPT-4</option>
      <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
      <option value="gpt-4-turbo">GPT-4 Turbo</option>
    `;
  } else {
    modelSelect.innerHTML = `<option value="custom">Custom Model</option>`;
  }
});

input.addEventListener('input', () => {
  input.style.height = 'auto';
  input.style.height = Math.min(input.scrollHeight, 120) + 'px';
});

// Initialize
input.focus();
</script>
</body>
</html>
