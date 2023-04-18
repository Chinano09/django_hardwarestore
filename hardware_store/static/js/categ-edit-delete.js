function deleteCategory(categoryId) {
    let path = "delete_category/" + categoryId;
    location.replace(path);
 }
 
 function editCategory(categoryId) {
   let path = "edit_category/" + categoryId;
   location.replace(path);
 }

 function productCategory(categoryId) {
  let path = "product_list/" + categoryId + "/";
  location.replace(path);
}