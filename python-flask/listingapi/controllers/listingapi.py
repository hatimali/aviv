from typing import Tuple

from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound

from listingapi import registry
from listingapi.domain.entities.listings import ListingEntity, ListingPriceEntity
from listingapi.domain.exceptions.listings import ListingNotFoundException


app = Flask(__name__)
cors = CORS(app)


@app.route("/listings", methods=["GET"])
def get_listings() -> Tuple[Response, int]:
    """Get all listings."""
    listings_data = registry.retrieve_listings.perform()
    return jsonify(listings_data), 200


@app.route("/listings", methods=["POST"])
def post_listing() -> Tuple[Response, int]:
    """Create a listing."""
    data = request.get_json()
    listing = ListingEntity.parse_obj(data)
    listing_data = registry.persist_listing.perform(listing)
    listing_price = ListingPriceEntity.parse_obj(
        {"listing_id": listing_data["id"], "price": int(listing.latest_price_eur)}
    )
    registry.update_listing_price.perform(listing_price)
    return jsonify(listing_data), 201


@app.route("/listings/<int:id_>", methods=["PUT"])
def put_listing(id_: int) -> Tuple[Response, int]:
    """Update a listing."""
    data = request.get_json()
    listing = ListingEntity.parse_obj(data)
    listing_price = ListingPriceEntity.parse_obj(
        {"listing_id": id_, "price": int(listing.latest_price_eur)}
    )
    try:
        listing_data = registry.update_listing.perform(id_, listing)
        registry.update_listing_price.perform(listing_price)
    except ListingNotFoundException:
        raise NotFound
    return jsonify(listing_data), 200


@app.route("/listings/<int:id_>", methods=["DELETE"])
def delete_listing(id_: int) -> Tuple[Response, int]:
    """Delete a listing."""
    res = registry.delete_listing.perform(id_)
    return res, 200


@app.route("/listings/<int:id_>/prices", methods=["GET"])
def get_price_history(id_: int) -> Tuple[Response, int]:
    """Get price history."""
    """ Implement a new endpoint that will return the price changes for a given listing over time."""

    listing_prices_data = registry.retrieve_listing_prices.perform(id_)
    return jsonify(listing_prices_data), 200
