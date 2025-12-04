# Billing and Overdue Management Guide

## Overview
The Apartment Billing Management System provides comprehensive billing tracking and overdue payment management features.

---

## 1. HOW TO VIEW BILLINGS

### Access Billings
1. Login to the dashboard
2. Click **"📋 Billings"** in the sidebar under the **MAIN** section

### Billings View Features
- **Displays all active billings** with the following information:
  - Unit number and billing month
  - 💧 Water cost
  - ⚡ Electricity cost
  - 📡 WiFi cost
  - Total amount

### Example Display
```
📋 Unit 101 - 2024-12
💧 Water: ₱500.00 | ⚡ Electricity: ₱800.00 | 📡 WiFi: ₱300.00
Total: ₱1,600.00
```

### Create New Billing
1. Click **"📋 Create Billing"** button in the Billings view
2. Fill in the form:
   - **Unit Number**: Enter the unit (e.g., "101")
   - **Billing Month**: Format as YYYY-MM (e.g., "2024-12")
   - **Due Date**: Format as YYYY-MM-DD (e.g., "2024-12-31")
   - **Water Cost (₱)**: Enter water expense
   - **Electricity Cost (₱)**: Enter electricity expense
   - **WiFi Cost (₱)**: Enter WiFi expense
   - **Rent (₱)**: Enter rent amount
3. Click **"💾 Save Billing"**

---

## 2. HOW TO VIEW OVERDUE BILLINGS

### Access Overdue Section
1. Login to the dashboard
2. Click **"⚠️ Overdue Billings"** in the sidebar under the **REPORTS** section

### Overdue View Features
- **Shows all unpaid billings past their due date** with:
  - Tenant name
  - Amount due
  - Due date
  - Red highlighting to indicate urgency

### Example Display
```
⚠️ John Doe
Amount Due: ₱1,600.00 | Due Date: 2024-11-30

⚠️ Jane Smith  
Amount Due: ₱2,100.00 | Due Date: 2024-10-15
```

### Understanding Overdue Status
- A billing is considered **overdue** when:
  - The due date has passed
  - No payment has been made OR only partial payment has been made
  - The outstanding amount is greater than zero

---

## 3. PAYMENT HISTORY

### Access Payment History
1. Click **"💰 Payment History"** in the sidebar under the **REPORTS** section

### Payment History View
Shows all recorded payments with:
- Tenant ID
- Billing month
- Amount paid
- Payment method (CASH, CHECK, ONLINE, etc.)
- Payment date

### Example Display
```
| Tenant | Month     | Amount      | Method | Date       |
|--------|-----------|-------------|--------|------------|
| 001    | 2024-12   | ₱1,600.00   | CASH   | 2024-12-15 |
| 002    | 2024-12   | ₱2,100.00   | ONLINE | 2024-12-10 |
```

---

## 4. COLLECTION SUMMARY

### Access Collection Summary
1. Click **"📈 Collection Summary"** in the sidebar under the **REPORTS** section

### Collection Summary Metrics
- **Total Billings**: Number of billing records
- **Amount Due**: Total amount owed
- **Collected**: Total amount paid
- **Outstanding**: Amount still pending
- **Collection Rate**: Percentage of billings collected

---

## 5. MANAGING PAYMENTS

### Record a Payment
1. From the Payments section, click **"💳 Add Payment"**
2. Fill in:
   - **Tenant**: Select from dropdown
   - **Billing Month**: Select billing month
   - **Amount Paid (₱)**: Enter payment amount
   - **Payment Method**: Select (CASH, CHECK, ONLINE, etc.)
   - **Payment Date**: Select date
3. Click **"💾 Save Payment"**

### Track Payment Status
- Payments automatically update the billing status
- Once full payment is made, the billing shows as paid
- Partial payments show remaining balance

---

## 6. WORKFLOW EXAMPLE

### Scenario: Monthly Billing Process

**Step 1: Create Billing (Due: Dec 31)**
```
Unit 101
Water: ₱500
Electricity: ₱800
WiFi: ₱300
Rent: ₱20,000
Total: ₱21,600
```

**Step 2: Tenant Pays Partial (Dec 20)**
```
Payment: ₱10,000
Outstanding: ₱11,600
```

**Step 3: Check Overdue Report (Jan 5)**
```
⚠️ Unit 101 - Outstanding: ₱11,600 (Due: Dec 31)
```

**Step 4: Tenant Completes Payment (Jan 10)**
```
Payment: ₱11,600
Status: PAID ✓
```

**Step 5: Verify Collection Summary**
```
Collection Rate: 100% ✓
All units current
```

---

## 7. KEY METRICS TO MONITOR

| Metric | What It Shows | Action Needed |
|--------|---|---|
| Overdue Count | Number of unpaid billings | Follow up with tenants |
| Collection Rate | % of billings collected | Monitor for 80%+ target |
| Outstanding Amount | Total money pending | Send reminders |
| Days Overdue | How long payment is late | Escalate if >30 days |

---

## 8. TIPS FOR EFFECTIVE BILLING MANAGEMENT

✅ **Best Practices:**
- Create billings on the 1st of each month
- Set due dates 14-30 days after billing month
- Follow up on overdue payments within 5 days
- Accept multiple payment methods
- Keep detailed payment records
- Monitor collection rate trend

❌ **Avoid:**
- Creating duplicate billings
- Accepting cash without recording
- Forgetting to update payment status
- Missing overdue follow-ups
- Not keeping audit trail

---

## 9. TROUBLESHOOTING

### Overdue Billings Not Showing
- Check if payment was actually recorded
- Verify due date is in the past
- Ensure billing was created for that tenant

### Billings Not Appearing
- Verify tenant is active in the system
- Check if billing month is set correctly
- Ensure unit number exists

### Payment Not Reflecting
- Confirm payment was saved successfully
- Check payment date matches billing month
- Verify tenant ID is correct

---

## 10. DATA BACKUP RECOMMENDATIONS

- Backup database daily: `apartment_billing.db`
- Export payment records monthly
- Keep printed statements for audit trail
- Store sensitive payment info securely

