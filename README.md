# codebuild-parallel-pytest
This repository contains sample codes for running parallel pytest executions using AWS CodeBuild.

## Project Structure

Below is the file tree of the project, outlining its key components:

```
.
├── build
│   ├── buildspec_parallel.yaml  # Build specification for parallel execution
│   └── buildspec.yaml           # General build specification
├── README.md                    # (this file)
├── scripts
│   └── run_pytest_selected_part_with_arg_index.py  # Script to run a selected part of pytest files
└── tests
    └── unit
        ├── app
        │   ├── __init__.py
        │   ├── test_001.py
        │   ├── test_002.py
        │   └── test_003.py
        ├── __init__.py
        ├── test_001.py
        ├── test_002.py
        ├── test_003.py
        ├── test_004.py
        ├── test_005.py
        ├── test_006.py
        ├── test_007.py
        ├── test_008.py
        ├── test_009.py
        └── test_010.py
```

### Key Components

- **Build Specifications**: Located in the `build` directory. `buildspec_parallel.yaml` is specifically used for parallel execution setup.
- **Scripts**: Contains `run_pytest_selected_part_with_arg_index.py`, which is a script to run a designated part of pytest files based on argument index.
- **Pytest Files**: Located under `tests/unit`, these are simple pytest files named `test_001.py`, `test_002.py`, etc.

## CodeBuild Configuration Example

### Source Setup

- **GitHub**: Fork this repository and configure your Personal Access Token (PAT) and other settings as needed.
- **Amazon S3**: Compress the `build`, `scripts`, and `tests` in one zip file and upload them to your S3 bucket.

### Environment Setup

- **Image**: Managed Image
- **Compute Type**: EC2
- **Image Detail**: `aws/codebuild/amazonlinux2-x86_64-standard:4.0` (supports Python 3.9)

### Additional Configurations

- **Service Role**: Configure as required for your setup.
- **Buildspec Name**:  `build/buildspec_parallel.yaml`
- **Batch Configuration**: Enable
- **CloudWatch Logs**: Enable
