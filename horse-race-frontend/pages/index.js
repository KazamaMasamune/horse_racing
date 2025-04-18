import { useState } from 'react';

export default function Home() {
  const [formData, setFormData] = useState({
    actual_weight: '',
    declared_horse_weight: '',
    draw: '',
    win_odds: '',
    jockey_B_Prebble: false,
    jockey_C_Y_Ho: false,
    jockey_D_Whyte: false,
    jockey_J_Moreira: false,
    jockey_K_C_Leung: false,
    jockey_K_Teetan: false,
    jockey_M_L_Yeung: false,
    jockey_N_Callan: false,
    jockey_N_Rawiller: false,
    jockey_Z_Purton: false,
    jockey_Other: false,
  });
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const jockeys = ['jockey_B_Prebble', 'jockey_C_Y_Ho', 'jockey_D_Whyte', 'jockey_J_Moreira', 'jockey_K_C_Leung', 'jockey_K_Teetan', 'jockey_M_L_Yeung', 'jockey_N_Callan', 'jockey_N_Rawiller', 'jockey_Z_Purton', 'jockey_Other'];
    const selectedJockey = jockeys.find(j => formData[j]);

    if (!selectedJockey) {
      alert('Please select exactly one jockey.');
      return;
    }

    const data = {
      actual_weight: parseInt(formData.actual_weight),
      declared_horse_weight: parseInt(formData.declared_horse_weight),
      draw: parseInt(formData.draw),
      win_odds: parseFloat(formData.win_odds),
      ...Object.fromEntries(jockeys.map(j => [j, j === selectedJockey ? 1 : 0])),
    };

    try {
      const response = await fetch('http://localhost:5050/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      setPrediction(result.prediction);
    } catch (error) {
      console.error('Error:', error);
      setPrediction('Error making prediction');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4 text-center">Horse Race Winner Predictor</h1>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700">Actual Weight (lbs)</label>
            <input
              type="number"
              placeholder="e.g., 133"
              value={formData.actual_weight}
              onChange={(e) => setFormData({ ...formData, actual_weight: e.target.value })}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Declared Horse Weight (lbs)</label>
            <input
              type="number"
              placeholder="e.g., 1032"
              value={formData.declared_horse_weight}
              onChange={(e) => setFormData({ ...formData, declared_horse_weight: e.target.value })}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Draw (Starting Position)</label>
            <input
              type="number"
              placeholder="e.g., 1"
              value={formData.draw}
              onChange={(e) => setFormData({ ...formData, draw: e.target.value })}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Win Odds</label>
            <input
              type="number"
              step="0.1"
              placeholder="e.g., 3.8"
              value={formData.win_odds}
              onChange={(e) => setFormData({ ...formData, win_odds: e.target.value })}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2">Jockey</label>
            {['B Prebble', 'C Y Ho', 'D Whyte', 'J Moreira', 'K C Leung', 'K Teetan', 'M L Yeung', 'N Callan', 'N Rawiller', 'Z Purton', 'Other'].map(jockey => (
              <label key={jockey} className="block">
                <input
                  type="checkbox"
                  checked={formData[`jockey_${jockey.replace(/ /g, '_')}`]}
                  onChange={(e) => {
                    const updated = { ...formData };
                    ['jockey_B_Prebble', 'jockey_C_Y_Ho', 'jockey_D_Whyte', 'jockey_J_Moreira', 'jockey_K_C_Leung', 'jockey_K_Teetan', 'jockey_M_L_Yeung', 'jockey_N_Callan', 'jockey_N_Rawiller', 'jockey_Z_Purton', 'jockey_Other'].forEach(j => {
                      updated[j] = false;
                    });
                    updated[`jockey_${jockey.replace(/ /g, '_')}`] = e.target.checked;
                    setFormData(updated);
                  }}
                />
                {jockey}
              </label>
            ))}
          </div>
          <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
            Predict
          </button>
        </form>
        {prediction && (
          <p className="mt-4 text-center text-lg font-semibold">
            Prediction: {prediction}
          </p>
        )}
      </div>
    </div>
  );
}
