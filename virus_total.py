import logging
from fastapi import APIRouter

from common.content_types import ContentType
from common.response_data_handler import ResponseDataHandler
from common.fast_api_logger import fast_api_logger
from virus_total_resources import pop_irrelevant_relationships

URL_ENDPOINT: str = "url"
IP_ADDRESS_ENDPOINT: str = "ip-address"
REPORT_ENDPOINT: str = "report"
INVALID_FILE_HASH = "155837e476b50c93b6522b310a684a53"

router: APIRouter = APIRouter()
logger: logging.Logger = logging.getLogger(fast_api_logger)
_response_data_handler: ResponseDataHandler = ResponseDataHandler(mongo=True,
                                                                      collection_name="virus_total")

@router.get("/analyses/{query}")
async def enrich_analysed_result(query: str) -> dict:
    return _response_data_handler.get_responses_data_by_file_name(enrich_analysed_result.__name__+"_"+query,
                                                                  content_type=ContentType.JSON)

@router.get("/{collection_name}/{object_id}")
async def get_investigation_enrichment(collection_name: str, object_id: str, relationships: str) -> dict:
    return pop_irrelevant_relationships(
        relationships_data=_response_data_handler.get_response_data_by_source(
            get_investigation_enrichment.__name__,
            object_id,
            required_query=True), relationships_list=relationships)


@router.get("/get_investigation_enrichment_result")
async def get_investigation_enrichment_result(ip: str,
                                        relationships_list: str) -> dict:
    return pop_irrelevant_relationships(
        relationships_data=_response_data_handler.get_response_data_by_source(
            get_investigation_enrichment_result.__name__,
            ip,
            required_query=True), relationships_list=relationships_list)


@router.get("/search")
async def search(query: str) -> dict:
    return _response_data_handler.get_response_data_by_source(search.__name__, query,
                                                              required_query=True)


@router.get("/search_result")
async def search_result(query: str) -> dict:
    return _response_data_handler.get_response_data_by_source(search_result.__name__, query,
                                                              required_query=True)


@router.post("/files/{query}/analyse")
async def enrich_analyse_id_file_hash(query: str) -> dict:
    return _response_data_handler.get_responses_data_by_file_name(enrich_analyse_id_file_hash.__name__+"_"+query,
                                                                  content_type=ContentType.JSON)


@router.get("/results/reanalyse_file_hash/{file_hash_id}")
async def reanalyse_file_result(file_hash_id: str) -> dict:
    content_type: str = ContentType.JSON
    if file_hash_id == INVALID_FILE_HASH:
        content_type = ContentType.TEXT
    return _response_data_handler.get_responses_data_by_file_name(reanalyse_file_result.__name__ + "_" + file_hash_id,
                                                                  content_type=content_type)
