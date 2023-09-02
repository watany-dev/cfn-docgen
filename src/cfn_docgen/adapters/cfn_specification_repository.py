import json
from typing import List, Mapping
from cfn_docgen.config import AppContext

from cfn_docgen.domain.model.cfn_specification import CfnSpecificationForResource, CfnSpecificationPropertyTypeName, CfnSpecificationResourceTypeName, CfnSpecificationPropertyType, CfnSpecificationResourceType
from cfn_docgen.domain.model.cfn_specification import CfnSpecification
from cfn_docgen.domain.ports.cache import IFileCache
from cfn_docgen.domain.ports.internal.file_loader import IFileLoader
from cfn_docgen.domain.ports.cfn_specification_repository import ICfnSpecificationRepository


class CfnSpecificationRepository(ICfnSpecificationRepository):
    def __init__(
        self, 
        source_url:str,
        loader: IFileLoader, 
        cache: IFileCache, 
        recursive_resource_types:List[str],
        context:AppContext,
    ) -> None:
        self.context = context

        try:
            cached = cache.get(source_url)
            if cached is None:
                self.context.log_debug(f"cache not hit [{source_url}]")
                json_bytes = loader.download(source_url)
                json_str = json_bytes.decode()
                self.spec = CfnSpecification(**json.loads(json_str))
                cache.put(source_url, json_str)
            else:
                self.context.log_debug(f"cache hit [{source_url}]")
                self.spec = CfnSpecification(**json.loads(cached))
            self.recursive_resource_types = recursive_resource_types
        except Exception as ex:
            self.context.log_error("failed to setup CfnSpecificationRepository")
            raise ex


    def get_resource_spec(self, resource_type: CfnSpecificationResourceTypeName) -> CfnSpecificationResourceType:
        try:
            return self.spec.ResourceTypes[resource_type.fullname]
        except KeyError as ex:
            self.context.log_debug(f"Specification for resource tyoe [{resource_type.fullname}] is not found")
            raise ex

    def get_property_spec(self, property_type: CfnSpecificationPropertyTypeName) -> CfnSpecificationPropertyType:
        try:
            return self.spec.PropertyTypes[property_type.fullname]
        except KeyError as ex:
            self.context.log_debug(f"Specification for property tyoe [{property_type.fullname}] is not found")
            raise ex

    def list_properties_for_resource(self, resource_type: CfnSpecificationResourceTypeName) -> Mapping[str, CfnSpecificationPropertyType]:
        property_specs:Mapping[str, CfnSpecificationPropertyType] = {}
        for property_type, property_spec in self.spec.PropertyTypes.items():
            if property_type.startswith(f"{resource_type.fullname}.") or property_type == "Tag":
                property_specs[property_type] = property_spec
        return property_specs


    def get_specs_for_resource(self, resource_type: CfnSpecificationResourceTypeName) -> CfnSpecificationForResource:
        resource_spec = self.get_resource_spec(resource_type)
        property_specs = self.list_properties_for_resource(resource_type)
        return CfnSpecificationForResource(
            ResourceSpec=resource_spec,
            PropertySpecs=property_specs,
        )

    def is_recursive(self, resource_type: CfnSpecificationResourceTypeName) -> bool:
        if resource_type.fullname in self.recursive_resource_types:
            self.context.log_debug(f"resource type [{resource_type}] is recurisive resource")
            return True
        return False
