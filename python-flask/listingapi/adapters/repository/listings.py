from typing import Dict, List

from sqlalchemy.orm import scoped_session

from listingapi.adapters.mappers.listings import ListingMapper, ListingPriceMapper
from listingapi.adapters.repository.models.listings import Base, ListingModel, ListingPriceModel
from listingapi.domain.entities.listings import ListingEntity, ListingPriceEntity
from listingapi.domain.exceptions.listings import ListingNotFoundException
from listingapi.domain.ports.repository.listings import ListingRepository


class SqlAlchemyListingRepository(ListingRepository):
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        Base.metadata.create_all(self.db_session.get_bind())

    def create(self, listing: ListingEntity) -> Dict:
        listing_model = ListingMapper.from_entity_to_model(listing)
        self.db_session.add(listing_model)
        self.db_session.commit()
        data = ListingMapper.from_model_to_dict(listing_model)
        return data

    def delete(self, id_: int) -> Dict:
        listing = self.db_session.get(ListingModel, id_)
        if listing is None:
            return {"id": id_, "message": "Listing not found."}
        self.db_session.delete(listing)
        self.db_session.commit()
        return {"id": id_, "message": "Listing deleted successfully."}

    def get_all(self) -> List[Dict]:
        listing_models = self.db_session.query(ListingModel).all()
        listings = [
            ListingMapper.from_model_to_dict(listing) for listing in listing_models
        ]
        return listings

    def update(self, id_: int, listing: ListingEntity) -> Dict:
        existing_listing = self.db_session.get(ListingModel, id_)
        if existing_listing is None:
            raise ListingNotFoundException
        self.db_session.delete(existing_listing)

        listing_model = ListingMapper.from_entity_to_model(listing)
        listing_model.id = id_
        self.db_session.add(listing_model)
        self.db_session.commit()

        listing_dict = ListingMapper.from_model_to_dict(listing_model)
        return listing_dict

    def get_price(self, id_: int) -> Dict:
        price_models = self.db_session.query(ListingPriceModel).filter(ListingPriceModel.listing_id == id_)
        prices = [
            ListingPriceMapper.from_model_to_dict(listing_price) for listing_price in price_models
        ]
        return prices

    def update_price(self, obj: ListingPriceEntity) -> Dict:
        existing_prices = self.db_session.query(ListingPriceModel).filter(ListingPriceModel.listing_id == obj.listing_id)
        try:
            latest_price = [
                ListingPriceMapper.from_model_to_dict(listing_price) for listing_price in existing_prices
            ][-1]
            if int(latest_price['price']) == int(obj.price):
                return []
        except IndexError:
            pass
        listing_price_model = ListingPriceMapper.from_entity_to_model(obj)
        self.db_session.add(listing_price_model)
        self.db_session.commit()
        data = ListingPriceMapper.from_model_to_dict(listing_price_model)
        return data
