SELECT
    vendor_id,
    SUM(po_amount) AS total_spend,
    COUNT(*) AS total_orders
FROM purchase_orders
GROUP BY vendor_id
ORDER BY total_spend DESC;

SELECT
    vendor_id,
    SUM(po_amount) AS total_spend,
    COUNT(*) AS total_orders
FROM purchase_orders
GROUP BY vendor_id
ORDER BY total_spend DESC;

-- Invoice amount mismatch analysis
SELECT
    invoices.invoice_id,
    invoices.po_id,
    invoices.vendor_id,
    invoices.invoice_amount,
    purchase_orders.po_amount,
    invoices.invoice_amount - purchase_orders.po_amount
        AS amount_difference
FROM invoices
JOIN purchase_orders
    ON invoices.po_id = purchase_orders.po_id
WHERE invoices.invoice_amount > purchase_orders.po_amount
ORDER BY amount_difference DESC;

-- Duplicate invoice analysis
SELECT
    invoice_id,
    COUNT(*) AS occurrence_count,
    GROUP_CONCAT(po_id) AS purchase_orders,
    GROUP_CONCAT(vendor_id) AS vendors
FROM invoices
GROUP BY invoice_id
HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC;

-- Overall procurement analysis summary
SELECT
    (SELECT COUNT(*) FROM vendors) AS total_vendors,
    (SELECT COUNT(*) FROM purchase_orders) AS total_purchase_orders,
    (SELECT ROUND(SUM(po_amount), 2)
     FROM purchase_orders) AS total_spend,
    (SELECT COUNT(*)
     FROM invoices
     WHERE invoice_amount > (
         SELECT po_amount
         FROM purchase_orders
         WHERE purchase_orders.po_id = invoices.po_id
     )) AS invoices_above_po_amount,
    (SELECT COUNT(*)
     FROM (
         SELECT invoice_id
         FROM invoices
         GROUP BY invoice_id
         HAVING COUNT(*) > 1
     )) AS duplicated_invoice_ids;

