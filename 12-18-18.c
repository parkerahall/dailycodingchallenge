#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

typedef struct node {
    int value;
    struct node* both;
} node_t;

typedef struct list {
    node_t* head;
    node_t* tail;
    int length;
} list_t;

static node_t* START = (node_t*)0;
static node_t* END = (node_t*)1;

node_t* XOR(node_t* left, node_t* right) {
    return (node_t*)((uint64_t)left ^ (uint64_t)right);
}

void free_list(list_t* root) {
    if (root->head != NULL) {
        node_t* current_node = root->head;
        node_t* next_node = XOR(current_node->both, START);
        node_t* next_next_node;

        while (next_node != END) {
            next_next_node = XOR(next_node->both, current_node);

            free(current_node);

            current_node = next_node;
            next_node = next_next_node;
        }
    }
}

void add_element(list_t* root, int element) {
    node_t* new_node = malloc(sizeof(node_t));
    new_node->value = element;

    if (root->head == NULL) {
        new_node->both = XOR(START, END);
        root->head = new_node;
        root->tail = new_node;
    } else {
        new_node->both = XOR(root->tail, END);

        root->tail->both = XOR(root->tail->both, END);
        root->tail->both = XOR(root->tail->both, new_node);
        root->tail = new_node;
    }

    root->length++;
}

node_t* get(list_t* root, int index) {
    assert(root->length > index && index >= 0);

    node_t* current_node = root->head;
    node_t* next_node = XOR(current_node->both, START);
    node_t* next_next_node;

    while (index > 0) {
        next_next_node = XOR(next_node->both, current_node);
        current_node = next_node;
        next_node = next_next_node;

        index--;
    }
    return current_node;
}

int main(int argc, char* argv[]) {
    list_t l = {NULL, NULL, 0};
    add_element(&l, 7);
    add_element(&l, -3);

    printf("First element: %d\n", get(&l, 0)->value);
    printf("Second element: %d\n", get(&l, 1)->value);

    free_list(&l);

    return 0;
}