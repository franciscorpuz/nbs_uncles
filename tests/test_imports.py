"""Verify that all public names are importable from the top-level package."""


def test_top_level_imports():
    from nbs_uncles import (
        read_file,
        show_depth,
        build_coverage_mask,
        filter_blobs_keep_lines,
        filter_squares_keep_lines,
        filter_morphological_operations,
        compute_local_orientation,
        rotate_points,
        update_geotransform,
        refine_cluster_rotation,
        undo_rotation,
        x_distance,
        detect_trackline_positions,
        assign_depths_to_lines,
        process_line_pair,
        build_uncertainty_raster,
    )
    assert callable(read_file)
    assert callable(build_coverage_mask)
    assert callable(build_uncertainty_raster)


def test_subpackage_imports():
    from nbs_uncles.io import read_file
    from nbs_uncles.visualization import show_depth
    from nbs_uncles.preprocessing import build_coverage_mask
    from nbs_uncles.methods import spectral_estimator, statistical_estimator
    from nbs_uncles.pipeline import detect_trackline_positions
    assert callable(read_file)
    assert callable(show_depth)
    assert callable(build_coverage_mask)
    assert callable(spectral_estimator)
    assert callable(detect_trackline_positions)
