var pluralize = function (word , count) {
    if ( count === 1) {return word;}

    return word + 's'

};


var bulkSelectors= {
    'selectAll' : '#select_all',
    'checkedItems': '.checkbox-item',
    'colheader' : 'th.col_header',
    'selectedRow': "alert alert-warning",
    'updateScope': '#scope',
    'bulkActions': '#bulk_actions'
}


//onready 
$(document).ready(function () {
    console.log( "ready!" );   
  
// Bulk delete
$('body').on('change' , bulkSelectors.checkedItems,function() {
    var checkedSelector = bulkSelectors.checkedItems + ':checked';
    var itemCount = $(checkedSelector).length;
    var pluralizeItem = pluralize(' item' , itemCount);
    var scopeOptionText = itemCount + ' selected' + pluralizeItem;
    console.log(scopeOptionText)

    //$('th.col_header').hide();

    if ($(this).is(':checked')) {
        $(this).closest('tr').addClass(bulkSelectors.selectedRow);

        $(bulkSelectors.colheader).hide();
        
        $(bulkSelectors.bulkActions).show()
    }
    else {
        $(this).closest('tr').removeClass(bulkSelectors.selectedRow);

        if (itemCount === 0) {
            $(bulkSelectors.bulkActions).hide();
            $(bulkSelectors.colheader).show()
        }
    }

    $(bulkSelectors.updateScope + ' option:first').text(scopeOptionText);

    });


    $('body').on('change' , bulkSelectors.selectAll, function() {
        var checkedStatus = this.checked;
       // $('th.col_header').hide();
        $(bulkSelectors.checkedItems).each(function() {
            $(this).prop('checked' , checkedStatus);
            
            $(this).trigger('change');
        });

    });

});




