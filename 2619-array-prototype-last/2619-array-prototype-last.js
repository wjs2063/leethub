Array.prototype.last = function() {
    if (this.length){
        return this.pop();
    }
    return -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */