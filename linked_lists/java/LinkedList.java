class LinkedList {
    private Node head;
    public LinkedList() {
        this.head = null;
    }
    /**
     * add node to the end of the list
     */
    public void function add(Node v) {
        if(this.head==null) {
            this.head = v;
            return
        }
        
        tmp = this.head;
        while(tmp.next!=null) {
            tmp = tmp.next;
        }

        tmp.next = v;
        return
    }
    
}
