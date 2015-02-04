
function DragHandler(source_selector, target_selector) {
  this.dispatch = this.dispatcher(this);
  this.effect = 'copy';
  this.assign_events(source_selector, target_selector);
};

DragHandler.prototype.assign_events = function(source_selector, target_selector) {
  var source_element = document.querySelector(source_selector);
  source_element.addEventListener('dragstart', dispatch.dragstart);
  source_element.addEventListener('dragend', dispatch.dragend);
  
  var target_element = document.querySelector(target_selector);
  target_element.addEventListener('dragover', dispatch.dragover);
  target_element.addEventListener('drop', dispatch.drop);
};

DragHandler.prototype.dispatcher = function(handler) {
  return {
    dragstart: function(event) {
      handler.dragstart(this, event);
    },
    dragover: function(event) {
      handler.dragover(this, event);
    },
    drop: function(event) {
      handler.drop(this, event);
    },
    dragend: function(event) {
      handler.dragend(this, event);
    }
  };
}

DragHandler.prototype.dragstart = function(wrapper, event) {
  event.dataTransfer.effectAllowed = this.effect;
  this.dragSource = wrapper;
};

DragHandler.prototype.dragover = function(wrapper, event) {
  if (event.dataTransfer.effectAllowed != this.effect) {
    return;
  }
  event.preventDefault();
};

DragHandler.prototype.drop = function(wrapper, event) {
  event.preventDefault();
};

DragHandler.prototype.dragend = function(wrapper, event) {
  if (event.dataTransfer.dropEffect == 'none') {
    console.log('drag canceled');
  }
};

// ===========

function DragOrdering(ordering_selector) {
  DragHandler.call(this, ordering_selector, ordering_selector);
  var wrappers = document.querySelectorAll(ordering_selector + ' .drag-wrapper');
  function formClosure(order) {
    return function() { order.value = order.dataset.order; };
  }
  for(var iter = wrappers.length -1; iter >= 0; iter--) {
    var order = wrappers[iter].querySelector('input[name$=ORDER]');
    if (order.value) {
      break;
    }
    order.dataset.order = iter + 1;
    wrappers[iter].querySelector('textarea').addEventListener('change', formClosure(order));
  }
};

DragOrdering.prototype = Object.create(DragHandler.prototype);

DragOrdering.prototype.assign_events = function(source_selector, target_selector) {
  var wrappers = document.querySelectorAll(source_selector + ' .drag-wrapper');
  var iter = null, wrapper = null;
  for (iter=0; iter<wrappers.length; iter++) {
    wrapper = wrappers[iter];
    wrapper.addEventListener('dragstart', this.dispatch.dragstart);
    wrapper.addEventListener('dragend', this.dispatch.dragend);

    wrapper.addEventListener('dragover', this.dispatch.dragover);
    wrapper.addEventListener('drop', this.dispatch.drop);
  }
};

DragOrdering.prototype.dragstart = function(wrapper, event) {
  if (!event.target.classList.contains('anchor')) {
    event.preventDefault();
    return;
  }
  DragHandler.prototype.dragstart.call(this, wrapper, event);
  event.dataTransfer.setData('text/plain', event.target.textContent);
  wrapper.style.border = '1px dashed';
};

DragOrdering.prototype.dragover = function(wrapper, event) {
  if (!event.target.classList.contains('anchor')) {
    return;
  }
  DragHandler.prototype.dragover.call(this, wrapper, event);
};

DragOrdering.prototype.drop = function(wrapper, event) {
  if (!event.target.classList.contains('anchor')) {
    event.preventDefault();
    return;
  }
  DragHandler.prototype.drop.call(this, wrapper, event);
  wrapper.parentNode.insertBefore(this.dragSource, wrapper);
  this.reorder(wrapper, this.dragSource);
  event.dataTransfer.dropEffect = 'move';
};

DragOrdering.prototype.dragend = function(wrapper, event) {
  DragHandler.prototype.dragend.call(this, wrapper, event);
  if (event.dataTransfer.dropEffect == 'move') {
    wrapper.parentNode.removeChild(wrapper);
  }
  else {
    wrapper.style.border = "none";
  }
};

DragOrdering.prototype.reorder = function(fromElement, byElement) {
  var from_order = fromElement.querySelector('input[name$=ORDER]');
  byElement.querySelector('input[name$=ORDER]').value = from_order.value;
  var increment_order = parseInt(from_order.value) + 1;
  from_order.value = increment_order;
  while (fromElement = fromElement.nextSibling) {
    if (fromElement.tagName != 'DIV') {
      continue;
    }
    var order = fromElement.querySelector('input[name$=ORDER]');
    if (order.value) {
      order.value = ++increment_order;
    }
    else {
      break;
    }
  };
}

function formset_add(event) {
  event.preventDefault();
  var root = this.parentNode;
  var wrappers = root.querySelectorAll('.drag-wrapper');
  var newWrapper = wrappers[wrappers.length -1].cloneNode(true);
  var elements = newWrapper.querySelectorAll('[name^=paragraphs]');
  var prev_prefix = elements[0].name.match(/paragraphs-(\d+)-/);
  var new_order = parseInt(prev_prefix[1]) + 1;
  var new_prefix = 'paragraphs-' + new_order + '-';
  prev_prefix = prev_prefix[0];
  var textrea_element = null, order_element = null;

  for (var iter = 0; iter < elements.length; iter++) {
    elements[iter].name = elements[iter].name.replace(prev_prefix, new_prefix);
    elements[iter].id = elements[iter].id.replace(prev_prefix, new_prefix);
    if (elements[iter].name.match('ORDER')) {
      order_element = elements[iter];
      elements[iter].dataset.order = new_order + 1;
    }
    if (elements[iter].tagName == 'TEXTAREA') {
      textarea_element = elements[iter];
    }
  }
  
  textarea_element.addEventListener('change', 
    (function formClosure(order) {
      return function() { order.value = order.dataset.order; };
    })(order_element)
  );
  var anchor = newWrapper.querySelector('span.anchor');
  anchor.textContent = new_order + 1;
  anchor.draggable = true;
  root.insertBefore(newWrapper, this);

  var total_forms = root.parentNode.querySelector('input[name$=TOTAL_FORMS]');
  total_forms.value = parseInt(total_forms.value) + 1;
}
