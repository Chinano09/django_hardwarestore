function deleteProduct(productId) {
  let path = "delete_product/" + productId;
  location.replace(path);
}

function editProduct(productId) {
  let path = "edit_product/" + productId;
  location.replace(path);
}