/**
 * GroceryBud React App
 * Author: Priyanshu Verma
 */

import React, { useState, useEffect } from 'react'
import api from './services/api'
import './styles/App.css'

function App() {
  const [items, setItems] = useState([])
  const [newItem, setNewItem] = useState('')
  const [newQuantity, setNewQuantity] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [stats, setStats] = useState({ total_items: 0, purchased_items: 0, pending_items: 0 })

  useEffect(() => {
    fetchItems()
    fetchStats()
  }, [])

  const fetchItems = async () => {
    try {
      setLoading(true)
      const response = await api.get('items/')
      setItems(response.data.results || response.data)
      setError('')
    } catch (err) {
      setError('Error fetching items: ' + err.message)
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  const fetchStats = async () => {
    try {
      const response = await api.get('items/stats/')
      setStats(response.data)
    } catch (err) {
      console.error('Error fetching stats:', err)
    }
  }

  const addItem = async () => {
    if (!newItem.trim() || !newQuantity.trim()) {
      setError('Please enter both item name and quantity')
      return
    }

    try {
      const response = await api.post('items/', {
        name: newItem,
        quantity: newQuantity,
      })
      setItems([response.data.data, ...items])
      setNewItem('')
      setNewQuantity('')
      setError('')
      fetchStats()
    } catch (err) {
      setError('Error adding item: ' + err.message)
    }
  }

  const deleteItem = async (id) => {
    try {
      await api.delete(`items/${id}/`)
      setItems(items.filter((item) => item.id !== id))
      fetchStats()
    } catch (err) {
      setError('Error deleting item: ' + err.message)
    }
  }

  const togglePurchased = async (item) => {
    try {
      const response = await api.patch(`items/${item.id}/`, {
        purchased: !item.purchased
      })
      setItems(items.map((i) => (i.id === item.id ? response.data : i)))
      fetchStats()
    } catch (err) {
      setError('Error updating item: ' + err.message)
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🛒 Grocery Bud</h1>
        <p>Your simple grocery list tracker</p>
      </header>
      
      <main className="container">
        <div className="card">
          <h2>Manage Your Grocery List</h2>
          
          {error && <div className="error">{error}</div>}
          
          <div className="status">
            <div className="status-item">
              <span className="status-dot green"></span>
              <span>✅ Total: {stats.total_items} items</span>
            </div>
            <div className="status-item">
              <span className="status-dot yellow"></span>
              <span>⏳ Pending: {stats.pending_items} items</span>
            </div>
            <div className="status-item">
              <span className="status-dot blue"></span>
              <span>📦 Purchased: {stats.purchased_items} items</span>
            </div>
          </div>

          <div className="input-section">
            <div>
              <input
                type="text"
                value={newItem}
                onChange={(e) => setNewItem(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && addItem()}
                placeholder="Item name..."
                className="input"
              />
            </div>
            <div>
              <input
                type="text"
                value={newQuantity}
                onChange={(e) => setNewQuantity(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && addItem()}
                placeholder="Quantity..."
                className="input"
              />
            </div>
            <button onClick={addItem} className="btn btn-add">
              Add Item
            </button>
          </div>

          {loading ? (
            <p className="loading">Loading items...</p>
          ) : (
            <div className="items-list">
              {items.length === 0 ? (
                <p className="empty">No items yet. Add one to get started!</p>
              ) : (
                items.map((item) => (
                  <div key={item.id} className={`item ${item.purchased ? 'purchased' : ''}`}>
                    <div className="item-content">
                      <input
                        type="checkbox"
                        checked={item.purchased}
                        onChange={() => togglePurchased(item)}
                        className="item-checkbox"
                      />
                      <div className="item-details">
                        <span className="item-name">{item.name}</span>
                        <span className="item-quantity">Qty: {item.quantity}</span>
                      </div>
                    </div>
                    <button
                      onClick={() => deleteItem(item.id)}
                      className="btn btn-delete"
                    >
                      Delete
                    </button>
                  </div>
                ))
              )}
            </div>
          )}

          <footer className="footer">
            <p>GroceryBud © 2026</p>
            <p>Author: Priyanshu Verma</p>
          </footer>
        </div>
      </main>
    </div>
  )
}

export default App
