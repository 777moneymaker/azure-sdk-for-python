# Azure SDK Refactor

## Refactoring BUILD and VERSIONING into the `azure-sdk-tools` package for easy reuse and testing

While this is happening:

- [ ] Add Tests For Tricky Functions
- [ ] Add Type Hinting and Doc Comments (not enforcing parameter docstrings at this time)

Goals for the refactor:

- [ ] Refactor `build` of packages (including conda packages) into command `sdk_build` accessible from `azure-sdk-tools`
- [ ] Move necessary functions to support versioning (both requirement and package version updates) and build into `azure-sdk-tools`. Where a function has been moved out of `sanitize_setup.py` or `common_tasks.py`, call sites on _existing_ checks should be updated in place. So this means the current update takes care of updating versions and requirements + build. That's it. 
  - [ ] We will leave the current implementation of set_dev_version which simply updates package versions to daily alpha. That will be named sdk_build_version
- [ ] Make `versioning` commands available in commands `sdk_version_X`
- [ ] All functions should use CWD to establish where the root of the repository is or accept `--repo` as an argument which overrides that default.
- [ ] Introduce --buildURL cli command that will _reproduce_ an error or build or scenario from a devops build URL.

Minutae
- [ ] Move `sanitize_setup` functions into `functions.py`
- [ ] Make a pass over all moved entry scripts. Ensure standardized arguments are present and working.
- [ ] Document new environment variables
- [ ] Update the usings in tox_harness. Ton of dependencies that need to be cleaned up.

## Refactoring how we install required packages for `regression`, `min/latestdependency` and any of our test scenarios

Right now we essentially follow the standard of:

- Create tox environment based on preseeded requirements from earlier in the CI pipeline
- `[CI ONLY]` Process dev_requirements.txt to reduce relative dependencies to absolute paths to pre-built wheels (this avoids parallel access errors that WILL randomly happen within the parallel tox runs)
- Check dev_requirements.txt against actual package requirements. If we are running an environment that mandates specific package dependencies be installed (like minimum or latest), remove those requirements from the dev_requirements.txt.
- Install dev_requirements.txt and ci_tools.txt
- If necessary install specific requirements
- Install the package (from artifact directory or built at runtime)

What we _want_ is to have a scenario generator that offers the _options_ that we SHOULD test exposed as CLI arguments to command `sdk_scenario`.

We want to take into account:
- 1 or multiple dev feeds
- A prebuilt artifact directory or not for the package we are generating a scenario for
- Whether or not we are allowing `alpha` versioned dependendencies
- A `scenario`. Be it `latest`, `minimum`, `whl`, `sdist`

The method:

1. Examine the package. Are we grabbing it from a prebuilt directory? Are we in `dev_mode` (alpha versioned and requirements allow alpha) 
  - Add the resolved package reference to a `scenario.txt` 
2. Examine our dev_requirements. Do we need to do any pre-processing like we currently do in `tox_harness.py`? 
 - Pass set of requirements to the next phase.
3. Process package requirements.
  - Are we in dev mode? That affects our search
  - Select which versions of the requirements should be installed
  - Any requirements resolved in this phase supplant those in the dictionary passed from phase 2. 
  - Pass combination requirements to next phase.
4. Combine stripped down tox_environment_requirements.txt file to combination, with previous values holding weight over values from tox_environment_requirements.txt
5. Write entire combination of requirements to `scenario_name.txt`
6. The tox environment should install only azure_sdk_tools to start with, invoke `scenario_generator`, then install _that_ file. 
7. Check for the presence of a `ci_constraints.txt` which pins certain versions to help with test failures in CI.
8. Invoke tests as normal

## Refactor test invocation 
