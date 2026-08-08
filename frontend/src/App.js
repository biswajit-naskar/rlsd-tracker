import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
import { Pie, Bar } from 'react-chartjs-2';
import './App.css';

Chart.register(...registerables);

const API_BASE = 'http://localhost:8000/api/v1';

function App() {
  const [beneficiaries, setBeneficiaries] = useState([]);
  const [programs, setPrograms] = useState([]);
  const [assessments, setAssessments] = useState([]);
  const [feedback, setFeedback] = useState([]);
  const [employment, setEmployment] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchAllData();
  }, []);

  const fetchAllData = async () => {
    try {
      const [beneficiariesRes, programsRes, assessmentsRes, feedbackRes, employmentRes] = await Promise.all([
        axios.get(`${API_BASE}/beneficiaries/`),
        axios.get(`${API_BASE}/programs/`),
        axios.get(`${API_BASE}/assessments/`),
        axios.get(`${API_BASE}/feedback/`),
        axios.get(`${API_BASE}/employment/`)
      ]);

      setBeneficiaries(beneficiariesRes.data);
      setPrograms(programsRes.data);
      setAssessments(assessmentsRes.data);
      setFeedback(feedbackRes.data);
      setEmployment(employmentRes.data);
      setLoading(false);
    } catch (err) {
      setError('Error fetching data. Make sure the backend server is running on port 8000.');
      setLoading(false);
    }
  };

  // Calculate statistics
  const totalBeneficiaries = beneficiaries.length;
  const totalPrograms = programs.length;
  const totalAssessments = assessments.length;
  const totalFeedback = feedback.length;
  const totalEmployment = employment.length;

  const maleCount = beneficiaries.filter(b => b.gender === 'Male').length;
  const femaleCount = beneficiaries.filter(b => b.gender === 'Female').length;

  const genderChartData = {
    labels: ['Male', 'Female'],
    datasets: [
      {
        data: [maleCount, femaleCount],
        backgroundColor: ['#2196F3', '#FF4081'],
        borderWidth: 1,
      },
    ],
  };

  // Assessment grade distribution
  const gradeCounts = { A: 0, B: 0, C: 0, D: 0, F: 0 };
  assessments.forEach(a => {
    if (a.grade) gradeCounts[a.grade] = (gradeCounts[a.grade] || 0) + 1;
  });

  const gradeChartData = {
    labels: ['A', 'B', 'C', 'D', 'F'],
    datasets: [
      {
        label: 'Grades',
        data: [gradeCounts.A, gradeCounts.B, gradeCounts.C, gradeCounts.D, gradeCounts.F],
        backgroundColor: ['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336'],
        borderWidth: 1,
      },
    ],
  };

  // Feedback satisfaction
  const avgSatisfaction = feedback.length > 0 
    ? (feedback.reduce((sum, f) => sum + f.satisfaction_score, 0) / feedback.length).toFixed(1)
    : 0;

  const avgQuality = feedback.length > 0
    ? (feedback.reduce((sum, f) => sum + f.training_quality, 0) / feedback.length).toFixed(1)
    : 0;

  // Employment status distribution
  const employmentStatus = {};
  employment.forEach(e => {
    employmentStatus[e.employment_status] = (employmentStatus[e.employment_status] || 0) + 1;
  });

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="App">
      <header className="header">
        <h1>🌾 RLSD-Tracker Dashboard</h1>
        <p>Rural Livelihood & Skill Development Tracker - MEAL Platform</p>
      </header>

      {/* Stats Cards */}
      <div className="stats">
        <div className="stat-card blue">
          <h3>Beneficiaries</h3>
          <p className="number">{totalBeneficiaries}</p>
        </div>
        <div className="stat-card green">
          <h3>Programs</h3>
          <p className="number">{totalPrograms}</p>
        </div>
        <div className="stat-card orange">
          <h3>Assessments</h3>
          <p className="number">{totalAssessments}</p>
        </div>
        <div className="stat-card purple">
          <h3>Feedback</h3>
          <p className="number">{totalFeedback}</p>
        </div>
        <div className="stat-card teal">
          <h3>Employment</h3>
          <p className="number">{totalEmployment}</p>
        </div>
      </div>

      {/* Charts Row */}
      <div className="charts-row">
        <div className="chart-container">
          <h2>👥 Gender Distribution</h2>
          {totalBeneficiaries > 0 ? (
            <Pie data={genderChartData} />
          ) : (
            <p>No data available</p>
          )}
        </div>

        <div className="chart-container">
          <h2>📊 Assessment Grades</h2>
          {totalAssessments > 0 ? (
            <Bar data={gradeChartData} />
          ) : (
            <p>No assessment data</p>
          )}
        </div>
      </div>

      {/* Feedback & Employment Stats */}
      <div className="stats-row">
        <div className="stat-card light">
          <h3>⭐ Average Satisfaction</h3>
          <p className="number">{avgSatisfaction}/5</p>
        </div>
        <div className="stat-card light">
          <h3>🎯 Training Quality</h3>
          <p className="number">{avgQuality}/5</p>
        </div>
        <div className="stat-card light">
          <h3>💼 Employment Status</h3>
          <p className="number">{Object.keys(employmentStatus).length}</p>
          <small>{Object.entries(employmentStatus).map(([k, v]) => `${k}: ${v}`).join(', ')}</small>
        </div>
      </div>

      {/* Beneficiaries Table */}
      <div className="table-container">
        <h2>📋 Beneficiaries List</h2>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Gender</th>
              <th>Block</th>
              <th>District</th>
              <th>Income</th>
            </tr>
          </thead>
          <tbody>
            {beneficiaries.length === 0 ? (
              <tr>
                <td colSpan="6" style={{ textAlign: 'center' }}>No beneficiaries found</td>
              </tr>
            ) : (
              beneficiaries.map((b) => (
                <tr key={b.id}>
                  <td>{b.beneficiary_id}</td>
                  <td>{b.full_name}</td>
                  <td>{b.gender}</td>
                  <td>{b.block}</td>
                  <td>{b.district}</td>
                  <td>₹{b.family_income}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;