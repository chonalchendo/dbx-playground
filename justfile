docker := require("docker")
rm := require("rm")
uv := require("uv")


PACKAGE := "dbx_playground"
REPOSITORY := "dbx_playground"
SOURCES := "src"
TESTS := "tests"
DBT := "dbt"

default:
    @just --list

import "tasks/check.just"
import "tasks/clean.just"
import "tasks/commit.just"
import "tasks/dbt.just"
import "tasks/format.just"
import "tasks/install.just"
import "tasks/package.just"
import "tasks/terraform.just"
