# API Docs

## GET *restaurant/*
Home page, serves static files

## GET *admin/*
Django admin interface

## Endpoint *auth/*
Includes all djoser implemented endpoints.
Some of the most important are:

###  POST *auth/users/*
Creates a new user. Request body must contain at least two fields: "username" and "password"

### POST *auth/token/login/*
Generates a token for a certain user. Request body must contain two fields: "username" and "password"

## POST *api-token-auth/*
The same as *auth/token/login/*

## GET *restaurant/menu/*
Shows all available menu items. Doesn't require authentication.

## POST *restaurant/menu/*
Creates new menu item. Requires authentication. Request body must contain three fields: "title", "price", "inventory".

## GET *restaurant/menu/<id>*
Shows menu item with a given id. Doesn't require authentication.

## DELETE, PUT *restaurant/menu/<id>*
Deletes or updates menu item with a given id. Required authentication.

## POST *restaurant/booking*
Creates a new booking record. Requires authentication. Request body should contain three fields: "name", "number_of_guests", "booking_date".

## GET *restaurant/booking*
Shows all bookings made. Requires authentication.