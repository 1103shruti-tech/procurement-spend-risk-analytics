-- PROCUREMENT SPEND AND VENDOR RISK ANALYTICS
-- Business Analysis Queries
-- Dataset: Synthetic procurement data

-- 1. TOP 5 VENDORS BY PROCUREMENT SPEND

SELECT
    vendor_id,
    ROUND(SUM(po_amount), 2) AS total_spend,
    COUNT(*) AS total_orders,
    ROUND(
        SUM(po_amount) * 100.0 /
        (SELECT SUM(po_amount) FROM purchase_orders),
        2
    ) AS spend_percentage
FROM purchase_orders
GROUP BY vendor_id
ORDER BY total_spend DESC
LIMIT 5;


-- 2. VENDOR AVERAGE PURCHASE ORDER VALUE

SELECT
    vendor_id,
    COUNT(*) AS total_orders,
    ROUND(AVG(po_amount), 2) AS average_order_value,
    ROUND(SUM(po_amount), 2) AS total_spend
FROM purchase_orders
GROUP BY vendor_id
ORDER BY average_order_value DESC
LIMIT 10;


-- 3. INVOICE AMOUNT DISCREPANCIES

SELECT
    i.invoice_id,
    i.vendor_id,
    i.invoice_amount,
    p.po_amount,
    ROUND(i.invoice_amount - p.po_amount, 2)
        AS amount_difference
FROM invoices i
JOIN purchase_orders p
    ON i.po_id = p.po_id
WHERE i.invoice_amount > p.po_amount
ORDER BY amount_difference DESC;


-- 4. DUPLICATE INVOICE IDENTIFICATION

SELECT
    invoice_id,
    COUNT(*) AS occurrence_count,
    GROUP_CONCAT(po_id) AS purchase_orders,
    GROUP_CONCAT(vendor_id) AS vendors
FROM invoices
GROUP BY invoice_id
HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC;


-- 5. VENDOR-WISE PAYMENT SUMMARY

SELECT
    i.vendor_id,
    COUNT(p.payment_id) AS total_payments,
    ROUND(SUM(p.payment_amount), 2) AS total_paid
FROM payments p
JOIN invoices i
    ON p.invoice_id = i.invoice_id
GROUP BY i.vendor_id
ORDER BY total_paid DESC;


-- 6. PURCHASE ORDER QUANTITY COMPLIANCE

SELECT
    COUNT(*) AS total_orders,
    SUM(
        CASE
            WHEN p.quantity_ordered = r.quantity_received
            THEN 1 ELSE 0
        END
    ) AS fully_received_orders,
    ROUND(
        SUM(
            CASE
                WHEN p.quantity_ordered = r.quantity_received
                THEN 1.0 ELSE 0
            END
        ) * 100 / COUNT(*),
        2
    ) AS compliance_percentage
FROM purchase_orders p
JOIN receipts r
    ON p.po_id = r.po_id;


-- 7. PURCHASE ORDER VS RECEIPT QUANTITY MISMATCHES

SELECT
    p.po_id,
    p.vendor_id,
    p.quantity_ordered,
    r.quantity_received,
    p.quantity_ordered - r.quantity_received
        AS quantity_difference
FROM purchase_orders p
JOIN receipts r
    ON p.po_id = r.po_id
WHERE p.quantity_ordered != r.quantity_received;


-- 8. PROCUREMENT DATA SUMMARY

SELECT
    (SELECT COUNT(*) FROM vendors) AS total_vendors,
    (SELECT COUNT(*) FROM purchase_orders) AS total_purchase_orders,
    (SELECT ROUND(SUM(po_amount), 2)
     FROM purchase_orders) AS total_procurement_spend,
    (SELECT COUNT(*) FROM invoices) AS total_invoices,
    (SELECT COUNT(*) FROM payments) AS total_payments,
    (SELECT COUNT(*)
     FROM invoices
     WHERE invoice_amount > (
         SELECT po_amount
         FROM purchase_orders
         WHERE purchase_orders.po_id = invoices.po_id
     )) AS invoices_above_po_amount;