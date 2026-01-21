/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { Orderline } from "@point_of_sale/app/store/models";

/**
 * Helper method to clear unpaid payment lines from an order.
 * Only removes payment lines that are not paid/sent/finalized.
 * 
 * @param {Order} order - The order instance
 */
function clearUnpaidPaymentLines(order) {
    // Guard: Only proceed if order exists and is editable
    if (!order || order.finalized || order.locked) {
        return;
    }

    // Guard: Only proceed if there are payment lines
    const paymentlines = order.get_paymentlines();
    if (!paymentlines || paymentlines.length === 0) {
        return;
    }

    // Filter out payment lines that are already paid/sent/finalized
    // A payment line is considered "paid" if:
    // 1. It has payment_status "done" or "reversed" (checked via is_done())
    // 2. The order is already finalized/paid
    const unpaidLines = [];
    for (const paymentLine of paymentlines) {
        // Check if payment is done/sent using the is_done() method
        // is_done() returns true if payment_status is "done" or "reversed", or if no status exists
        // We need to be more specific: only keep lines that are NOT done
        const paymentStatus = paymentLine.get_payment_status();
        const isPaymentDone = paymentStatus === "done" || paymentStatus === "reversed";
        
        // Only clear lines that are NOT done/sent
        if (!isPaymentDone) {
            unpaidLines.push(paymentLine);
        }
    }

    // Remove all unpaid payment lines
    // We need to remove them in reverse order to avoid index issues
    for (let i = unpaidLines.length - 1; i >= 0; i--) {
        order.remove_paymentline(unpaidLines[i]);
    }
}

/**
 * Patch Order model to clear unpaid payment lines when order is modified
 */
patch(Order.prototype, {
    /**
     * Override add_product to clear unpaid payment lines when a product is added
     */
    async add_product(product, options) {
        // Clear unpaid payment lines before adding product
        clearUnpaidPaymentLines(this);
        
        // Call original method
        return await super.add_product(...arguments);
    },

    /**
     * Override removeOrderline to clear unpaid payment lines when a product is removed
     */
    removeOrderline(line) {
        // Clear unpaid payment lines before removing orderline
        clearUnpaidPaymentLines(this);
        
        // Call original method
        return super.removeOrderline(...arguments);
    },
});

/**
 * Patch Orderline model to clear unpaid payment lines when orderline is modified
 */
patch(Orderline.prototype, {
    /**
     * Override set_quantity to clear unpaid payment lines when quantity changes
     */
    set_quantity(quantity, keep_price) {
        // Guard: Only clear if order exists and is not finalized
        if (this.order && !this.order.finalized && !this.order.locked) {
            clearUnpaidPaymentLines(this.order);
        }
        
        // Call original method
        return super.set_quantity(...arguments);
    },

    /**
     * Override set_unit_price to clear unpaid payment lines when price changes
     */
    set_unit_price(price) {
        // Guard: Only clear if order exists and is not finalized
        if (this.order && !this.order.finalized && !this.order.locked) {
            clearUnpaidPaymentLines(this.order);
        }
        
        // Call original method
        return super.set_unit_price(...arguments);
    },

    /**
     * Override set_discount to clear unpaid payment lines when discount changes
     */
    set_discount(discount) {
        // Guard: Only clear if order exists and is not finalized
        if (this.order && !this.order.finalized && !this.order.locked) {
            clearUnpaidPaymentLines(this.order);
        }
        
        // Call original method
        return super.set_discount(...arguments);
    },
});
