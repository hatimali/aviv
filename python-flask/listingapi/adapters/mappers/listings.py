from listingapi.adapters.repository.models.listings import ListingModel, ListingPriceModel
from listingapi.domain.entities.listings import ListingEntity, ListingPriceEntity


class ListingMapper:
    @staticmethod
    def from_entity_to_model(listing: ListingEntity) -> ListingModel:
        listing_model = ListingModel(
            name=listing.name,
            street_address=listing.postal_address.street_address,
            postal_code=listing.postal_address.postal_code,
            city=listing.postal_address.city,
            country=listing.postal_address.country,
            description=listing.description,
            building_type=listing.building_type,
            price=listing.latest_price_eur,
            surface_area_m2=listing.surface_area_m2,
            rooms_count=listing.rooms_count,
            bedrooms_count=listing.bedrooms_count,
            contact_phone_number=listing.contact_phone_number,
        )
        return listing_model

    @staticmethod
    def from_model_to_dict(listing: ListingModel) -> dict:
        listing_dict = {
            "id": listing.id,
            "name": listing.name,
            "postal_address": {
                "street_address": listing.street_address,
                "postal_code": listing.postal_code,
                "city": listing.city,
                "country": listing.country,
            },
            "description": listing.description,
            "building_type": listing.building_type,
            "latest_price_eur": listing.price,
            "surface_area_m2": listing.surface_area_m2,
            "rooms_count": listing.rooms_count,
            "bedrooms_count": listing.bedrooms_count,
            "contact_phone_number": listing.contact_phone_number,
            "created_date": listing.created_date.isoformat(),
            "updated_date": listing.updated_date.isoformat(),
        }
        return listing_dict


class ListingPriceMapper:
    @staticmethod
    def from_entity_to_model(obj: ListingPriceEntity) -> ListingPriceModel:
        listing_model = ListingPriceModel(
            listing_id=obj.listing_id,
            price=obj.price
        )
        return listing_model

    @staticmethod
    def from_model_to_dict(obj: ListingPriceModel) -> dict:
        listing_dict = {
            "id": obj.id,
            "listing_id": obj.listing_id,
            "price": obj.price,
            "created_date": obj.created_date.isoformat(),
        }
        return listing_dict

