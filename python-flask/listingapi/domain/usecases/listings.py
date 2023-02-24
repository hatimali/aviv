from typing import Dict, List

from listingapi.domain.entities.listings import ListingEntity, ListingPriceEntity
from listingapi.domain.ports.repository.listings import ListingRepository


class PersistListing:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing: ListingEntity) -> Dict:
        listing_dict = self.listing_repository.create(listing)
        return listing_dict


class RetrieveListings:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self) -> List[Dict]:
        listings = self.listing_repository.get_all()
        return listings


class RetrieveListingPrices:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, id_: int) -> List[Dict]:
        listing_price_dict = self.listing_repository.get_price(id_)
        return listing_price_dict


class UpdateListing:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, id_: int, listing: ListingEntity) -> Dict:
        listing_dict = self.listing_repository.update(id_, listing)
        return listing_dict


class UpdateListingPrice:
    def __init__(self, listing_repository: ListingRepository) -> None:
        self.listing_repository = listing_repository

    def perform(self, obj: ListingPriceEntity) -> Dict:
        listing_price_dict = self.listing_repository.update_price(obj)
        return listing_price_dict


class DeleteListing:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing: ListingEntity) -> Dict:
        listing_dict = self.listing_repository.delete(listing)
        return listing_dict
