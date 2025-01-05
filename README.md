barbEDI
=======

## How to run
You can specify the file you want to convert on the command line.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 json_to_edi.py <path_to_json_file>
```

## Structure
barbiedi/
 => constants.py
 => core/ (Functions to generate EDI segments)
	=> address_segment.py
	=> billing_provider_loop.py
	=> claim_information_loop.py
	=> contact_information_segment.py
	=> dependent_loop.py
	=> entity_segment.py
	=> professional_service_segment.py
	=> rendering_provider_segment.py
	=> service_facility_location_segment.py
	=> service_line_loop.py
	=> subscriber_loop.py
 => examples/
	=> mojo_dojo_casa_house.837
	=> mojo_dojo_casa_house.json
	=> multi_procedure_barbie.837
	=> multi_procedure_barbie.json
	=> subscriber_with_a_dekendent.837
	=> subscriber_with_a_dekendent.json
 => models/ (Pydantic models to validate JSON data)
	=> address.py
	=> base.py (Base model for all models)
	=> claim.py (Root model for a claim JSON file)
	=> claim_information.py
	=> contact_information.py
	=> entity.py (Contains multiple defined entities)
	=> patient.py
	=> service_line.py
 => json_to_edi.py
 => util/
	=> get_hierarchical_levels.py
 => .gitignore
 => README.md
 => requirements.txt
 => tests
 => .env

As this library grows, I would like to restructure this codebase to group the code by area such as 'providers', 'patients', 'claims', etc. But for now it 
feels more readable to have a simpler structure.

The `examples` folder includes three example JSON files and the 837 files that they generate.

**Note**
The beginning envelope of the 837 Professional claim — the interchange, group set, and transaction set portions — are provided in `edi_to_json`. To cut down on implementation time, you may copy/paste these into your implementation.