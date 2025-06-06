"""
Tests for the Marduk OpenCog Integration Analyzer
==================================================

These tests ensure that Marduk's theatrical cognitive analysis
capabilities function with the expected dramatic precision!
"""

import pytest
import os
import tempfile
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add the scripts directory to the path so we can import our analyzer
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from marduk_opencog_integration import MardukOpenCogAnalyzer


class TestMardukOpenCogAnalyzer:
    """🎭 Tests for the theatrical cognitive architecture analyzer! 🎭"""
    
    @pytest.fixture
    def temp_repo(self):
        """Create a temporary repository structure for testing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_path = Path(temp_dir)
            
            # Create the marduk prompt file
            marduk_prompt = {
                'messages': [
                    {'role': 'system', 'content': 'Marduk test content'},
                    {'role': 'user', 'content': 'test input'}
                ],
                'model': 'test-model',
                'modelParameters': {'max_tokens': 1000},
                'responseFormat': 'text'
            }
            
            import yaml
            with open(repo_path / 'marduk-v15.prompt.yml', 'w') as f:
                yaml.dump(marduk_prompt, f)
            
            # Create some test Python files with patterns
            test_files = {
                'memory_system.py': 'class MemoryCache:\n    def store(self, data):\n        pass',
                'task_executor.py': 'def execute_workflow(task):\n    process(task)',
                'ai_inference.py': 'class ModelInference:\n    def predict(self, input):\n        return model.forward(input)',
                'autonomous_agent.py': 'class AutoAdaptiveSystem:\n    def self_modify(self):\n        pass',
                'opencog_bridge.py': 'from atomspace import AtomSpace\ndef reasoning_engine():\n    pass'
            }
            
            for filename, content in test_files.items():
                with open(repo_path / filename, 'w') as f:
                    f.write(content)
            
            # Create a test YAML workflow
            workflow_content = {
                'name': 'Test Workflow',
                'jobs': {
                    'test': {
                        'steps': [{'run': 'echo test'}]
                    }
                }
            }
            
            workflows_dir = repo_path / '.github' / 'workflows'
            workflows_dir.mkdir(parents=True)
            with open(workflows_dir / 'test.yml', 'w') as f:
                yaml.dump(workflow_content, f)
            
            yield repo_path
    
    def test_marduk_analyzer_initialization(self, temp_repo):
        """Test that the Marduk analyzer initializes correctly! ⚡"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        assert analyzer.repo_path == temp_repo
        assert analyzer.marduk_prompt_path == temp_repo / 'marduk-v15.prompt.yml'
        assert analyzer.analysis_timestamp is not None
    
    def test_load_marduk_prompt_success(self, temp_repo):
        """Test successful loading of the Marduk prompt! 🧙‍♂️"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        prompt_data = analyzer.load_marduk_prompt()
        
        assert 'messages' in prompt_data
        assert 'model' in prompt_data
        assert prompt_data['model'] == 'test-model'
        assert len(prompt_data['messages']) == 2
    
    def test_load_marduk_prompt_missing_file(self, temp_repo):
        """Test handling of missing Marduk prompt file! 🚨"""
        # Remove the prompt file
        (temp_repo / 'marduk-v15.prompt.yml').unlink()
        
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        with pytest.raises(RuntimeError, match="THE MARDUK PROMPT HAS VANISHED"):
            analyzer.load_marduk_prompt()
    
    def test_analyze_repository_structure(self, temp_repo):
        """Test the repository structure analysis! 🔍"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        analysis = analyzer.analyze_repository_structure()
        
        # Check that analysis structure is correct
        assert 'cognitive_subsystems' in analysis
        assert 'opencog_integration_points' in analysis
        assert 'comfyui_workflow_connections' in analysis
        assert 'emergent_patterns' in analysis
        
        # Check cognitive subsystems
        subsystems = analysis['cognitive_subsystems']
        assert 'Memory' in subsystems
        assert 'Task' in subsystems
        assert 'AI' in subsystems
        assert 'Autonomy' in subsystems
        
        # Verify pattern detection worked
        assert len(subsystems['Memory']) > 0  # Should detect memory_system.py
        assert len(subsystems['Task']) > 0    # Should detect task_executor.py
        assert len(subsystems['AI']) > 0      # Should detect ai_inference.py
        assert len(subsystems['Autonomy']) > 0 # Should detect autonomous_agent.py
        
        # Check OpenCog integration detection
        assert len(analysis['opencog_integration_points']) > 0  # Should detect opencog_bridge.py
        
        # Check workflow detection
        assert len(analysis['comfyui_workflow_connections']) > 0  # Should detect test.yml
    
    def test_file_pattern_analysis(self, temp_repo):
        """Test the file pattern analysis functionality! 🧠"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        # Create analysis structure
        analysis = {
            "cognitive_subsystems": {"Memory": [], "Task": [], "AI": [], "Autonomy": []},
            "opencog_integration_points": [],
            "comfyui_workflow_connections": [],
            "emergent_patterns": []
        }
        
        # Test file with memory patterns
        file_path = temp_repo / 'test_memory.py'
        content = "class DataCache:\n    def store_in_memory(self, data):\n        self.cache[key] = data"
        
        analyzer._analyze_file_for_patterns(file_path, content, analysis)
        
        # Should detect memory pattern
        assert len(analysis['cognitive_subsystems']['Memory']) == 1
        assert analysis['cognitive_subsystems']['Memory'][0]['pattern'] == 'Memory management detected'
        assert analysis['cognitive_subsystems']['Memory'][0]['confidence'] == 'HIGH'
    
    def test_generate_theatrical_analysis(self, temp_repo):
        """Test the theatrical analysis report generation! 🎭"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        # Create test analysis data
        analysis = {
            "cognitive_subsystems": {
                "Memory": [{"file": "test.py", "pattern": "Test pattern", "confidence": "HIGH"}],
                "Task": [],
                "AI": [{"file": "ai.py", "pattern": "AI pattern", "confidence": "MEDIUM"}],
                "Autonomy": []
            },
            "opencog_integration_points": [
                {"file": "opencog.py", "opportunity": "Test opportunity", "details": "Test details"}
            ],
            "comfyui_workflow_connections": [
                {"file": "workflow.yml", "type": "Test workflow", "integration_potential": "HIGH"}
            ],
            "emergent_patterns": []
        }
        
        report = analyzer.generate_theatrical_analysis(analysis)
        
        # Verify theatrical elements are present
        assert "MARDUK'S MIND-BENDING OPENCOG INTEGRATION ANALYSIS" in report
        assert "BEHOLD!" in report
        assert "Maniacal laughter" in report
        assert "🎭" in report
        assert "🧠" in report
        assert "⚡" in report
        
        # Verify analysis content is included
        assert "Memory Subsystem" in report
        assert "AI Subsystem" in report
        assert "OPENCOG INTEGRATION NEXUS POINTS" in report
        assert "COMFYUI WORKFLOW SYMPHONY" in report
        assert "Test pattern" in report
        assert "Test opportunity" in report
    
    @patch('builtins.print')
    def test_run_analysis_success(self, mock_print, temp_repo):
        """Test successful execution of the complete analysis! 🎬"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        # Mock the time.sleep to speed up test
        with patch('time.sleep'):
            report = analyzer.run_analysis()
        
        # Verify the analysis completed
        assert report is not None
        assert "MARDUK'S MIND-BENDING OPENCOG INTEGRATION ANALYSIS" in report
        
        # Verify artifacts were created
        artifacts_dir = temp_repo / 'marduk_analysis_artifacts'
        assert artifacts_dir.exists()
        
        # Check that files were created
        json_files = list(artifacts_dir.glob('marduk_analysis_*.json'))
        report_files = list(artifacts_dir.glob('marduk_theatrical_report_*.md'))
        
        assert len(json_files) == 1
        assert len(report_files) == 1
        
        # Verify JSON file contains valid analysis data
        with open(json_files[0]) as f:
            saved_analysis = json.load(f)
        
        assert 'cognitive_subsystems' in saved_analysis
        assert 'opencog_integration_points' in saved_analysis
    
    def test_yaml_workflow_analysis(self, temp_repo):
        """Test YAML workflow file analysis! ⚙️"""
        analyzer = MardukOpenCogAnalyzer(str(temp_repo))
        
        analysis = {
            "cognitive_subsystems": {"Memory": [], "Task": [], "AI": [], "Autonomy": []},
            "opencog_integration_points": [],
            "comfyui_workflow_connections": [],
            "emergent_patterns": []
        }
        
        yaml_path = temp_repo / 'test_workflow.yml'
        content = {'jobs': {'test': {'steps': [{'run': 'echo test'}]}}}
        
        analyzer._analyze_yaml_for_workflows(yaml_path, content, analysis)
        
        assert len(analysis['comfyui_workflow_connections']) == 1
        assert analysis['comfyui_workflow_connections'][0]['type'] == 'GitHub Actions Workflow'
        assert analysis['comfyui_workflow_connections'][0]['integration_potential'] == 'HIGH'


def test_marduk_analyzer_import():
    """Test that the Marduk analyzer can be imported successfully! ✨"""
    from marduk_opencog_integration import MardukOpenCogAnalyzer
    
    # Verify the class exists and has the expected methods
    assert hasattr(MardukOpenCogAnalyzer, 'load_marduk_prompt')
    assert hasattr(MardukOpenCogAnalyzer, 'analyze_repository_structure')
    assert hasattr(MardukOpenCogAnalyzer, 'generate_theatrical_analysis')
    assert hasattr(MardukOpenCogAnalyzer, 'run_analysis')


def test_marduk_analyzer_with_real_repo():
    """Test the analyzer with the actual repository structure! 🌟"""
    # Get the repo root directory (assuming tests are run from repo root)
    repo_root = os.path.dirname(os.path.dirname(__file__))
    
    analyzer = MardukOpenCogAnalyzer(repo_root)
    
    # Test that it can load the real Marduk prompt
    prompt_data = analyzer.load_marduk_prompt()
    assert 'messages' in prompt_data
    assert 'Marduk' in prompt_data['messages'][0]['content']
    
    # Test that it can analyze the repository (but don't save artifacts in tests)
    analysis = analyzer.analyze_repository_structure()
    assert 'cognitive_subsystems' in analysis
    
    # Verify some patterns are detected in the real repo
    total_patterns = sum(len(findings) for findings in analysis['cognitive_subsystems'].values())
    assert total_patterns > 0  # Should find patterns in the actual codebase