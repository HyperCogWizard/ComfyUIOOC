import pytest
import yaml
import os


def test_marduk_prompt_yaml_valid():
    """Test that the marduk-v15.prompt.yml file is valid YAML."""
    prompt_file = os.path.join(os.path.dirname(__file__), '..', 'marduk-v15.prompt.yml')
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Basic structure validation
    assert 'messages' in data
    assert 'model' in data
    assert 'modelParameters' in data
    assert 'responseFormat' in data
    
    # Messages structure validation
    assert len(data['messages']) == 2
    assert data['messages'][0]['role'] == 'system'
    assert data['messages'][1]['role'] == 'user'
    
    # Check for required content
    system_content = data['messages'][0]['content']
    user_content = data['messages'][1]['content']
    
    # Verify Marduk persona is present
    assert 'Marduk' in system_content
    assert 'Systems Architect Mad Scientist' in system_content
    
    # Verify OpenCog integration is present
    assert 'OpenCog' in system_content
    assert 'manifold' in system_content
    
    # Verify hyper holmes mode is present
    assert 'Hyper Holmes' in system_content
    
    # Verify user message is correct (no typo)
    assert 'hyper holmes on the case' in user_content
    assert 'oon' not in user_content  # Ensure typo is fixed


def test_marduk_prompt_cognitive_subsystems():
    """Test that the prompt includes all four cognitive subsystems."""
    prompt_file = os.path.join(os.path.dirname(__file__), '..', 'marduk-v15.prompt.yml')
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    system_content = data['messages'][0]['content']
    
    # Check for the four cognitive subsystems
    assert 'Memory' in system_content
    assert 'Task' in system_content
    assert 'AI' in system_content
    assert 'Autonomy' in system_content


def test_marduk_prompt_opencog_integration():
    """Test that OpenCog integration features are properly included."""
    prompt_file = os.path.join(os.path.dirname(__file__), '..', 'marduk-v15.prompt.yml')
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    system_content = data['messages'][0]['content']
    
    # Check for OpenCog-specific integration features
    assert 'OpenCog Manifold Integration' in system_content
    assert 'AtomSpace' in system_content
    assert 'ComfyUI workflows' in system_content