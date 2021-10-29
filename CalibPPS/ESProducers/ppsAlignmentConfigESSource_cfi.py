import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource('PPSAlignmentConfigESSource',
  debug = cms.bool(False),
  label = cms.string(''),
  sequence = cms.vstring(),
  results_dir = cms.string('./alignment_results.txt'),
  sector_45 = cms.PSet(
    rp_N = cms.PSet(
      name = cms.string('L_1_F'),
      id = cms.int32(3),
      slope = cms.double(0.19),
      sh_x = cms.double(-3.6),
      x_min_fit_mode = cms.double(2),
      x_max_fit_mode = cms.double(7),
      y_max_fit_mode = cms.double(7),
      y_cen_add = cms.double(-0.3),
      y_width_mult = cms.double(1.1),
      x_slice_min = cms.double(7),
      x_slice_max = cms.double(19),
      x_slice_w = cms.double(0.2)
    ),
    rp_F = cms.PSet(
      name = cms.string('L_2_F'),
      id = cms.int32(23),
      slope = cms.double(0.19),
      sh_x = cms.double(-42),
      x_min_fit_mode = cms.double(2),
      x_max_fit_mode = cms.double(7.5),
      y_max_fit_mode = cms.double(7.5),
      y_cen_add = cms.double(-0.3),
      y_width_mult = cms.double(1.1),
      x_slice_min = cms.double(46),
      x_slice_max = cms.double(58),
      x_slice_w = cms.double(0.2)
    ),
    slope = cms.double(0.006),
    cut_h_apply = cms.bool(True),
    cut_h_a = cms.double(-1),
    cut_h_c = cms.double(-38.55),
    cut_h_si = cms.double(0.2),
    cut_v_apply = cms.bool(True),
    cut_v_a = cms.double(-1.07),
    cut_v_c = cms.double(1.63),
    cut_v_si = cms.double(0.15)
  ),
  sector_56 = cms.PSet(
    rp_N = cms.PSet(
      name = cms.string('R_1_F'),
      id = cms.int32(103),
      slope = cms.double(0.4),
      sh_x = cms.double(-2.8),
      x_min_fit_mode = cms.double(2),
      x_max_fit_mode = cms.double(7.4),
      y_max_fit_mode = cms.double(7.4),
      y_cen_add = cms.double(-0.8),
      y_width_mult = cms.double(1),
      x_slice_min = cms.double(6),
      x_slice_max = cms.double(17),
      x_slice_w = cms.double(0.2)
    ),
    rp_F = cms.PSet(
      name = cms.string('R_2_F'),
      id = cms.int32(123),
      slope = cms.double(0.39),
      sh_x = cms.double(-41.9),
      x_min_fit_mode = cms.double(2),
      x_max_fit_mode = cms.double(8),
      y_max_fit_mode = cms.double(8),
      y_cen_add = cms.double(-0.8),
      y_width_mult = cms.double(1),
      x_slice_min = cms.double(45),
      x_slice_max = cms.double(57),
      x_slice_w = cms.double(0.2)
    ),
    slope = cms.double(-0.015),
    cut_h_apply = cms.bool(True),
    cut_h_a = cms.double(-1),
    cut_h_c = cms.double(-39.26),
    cut_h_si = cms.double(0.2),
    cut_v_apply = cms.bool(True),
    cut_v_a = cms.double(-1.07),
    cut_v_c = cms.double(1.49),
    cut_v_si = cms.double(0.15)
  ),
  x_ali_sh_step = cms.double(0.01),
  y_mode_sys_unc = cms.double(0.03),
  chiSqThreshold = cms.double(50),
  y_mode_unc_max_valid = cms.double(5),
  y_mode_max_valid = cms.double(20),
  max_RP_tracks_size = cms.uint32(2),
  n_si = cms.double(4),
  matching = cms.PSet(
    reference_dataset = cms.string(''),
    rp_L_F = cms.PSet(
      sh_min = cms.double(-43),
      sh_max = cms.double(-41)
    ),
    rp_L_N = cms.PSet(
      sh_min = cms.double(-4.2),
      sh_max = cms.double(-2.4)
    ),
    rp_R_N = cms.PSet(
      sh_min = cms.double(-3.6),
      sh_max = cms.double(-1.8)
    ),
    rp_R_F = cms.PSet(
      sh_min = cms.double(-43.2),
      sh_max = cms.double(-41.2)
    )
  ),
  x_alignment_meth_o = cms.PSet(
    rp_L_F = cms.PSet(
      x_min = cms.double(47),
      x_max = cms.double(56.5)
    ),
    rp_L_N = cms.PSet(
      x_min = cms.double(9),
      x_max = cms.double(18.5)
    ),
    rp_R_N = cms.PSet(
      x_min = cms.double(7),
      x_max = cms.double(15)
    ),
    rp_R_F = cms.PSet(
      x_min = cms.double(46),
      x_max = cms.double(54)
    ),
    fit_profile_min_bin_entries = cms.uint32(5),
    fit_profile_min_N_reasonable = cms.uint32(10),
    meth_o_graph_min_N = cms.uint32(5),
    meth_o_unc_fit_range = cms.double(0.5)
  ),
  x_alignment_relative = cms.PSet(
    rp_L_F = cms.PSet(
      x_min = cms.double(0),
      x_max = cms.double(0)
    ),
    rp_L_N = cms.PSet(
      x_min = cms.double(7.5),
      x_max = cms.double(12)
    ),
    rp_R_N = cms.PSet(
      x_min = cms.double(6),
      x_max = cms.double(10)
    ),
    rp_R_F = cms.PSet(
      x_min = cms.double(0),
      x_max = cms.double(0)
    ),
    near_far_min_entries = cms.uint32(100)
  ),
  y_alignment = cms.PSet(
    rp_L_F = cms.PSet(
      x_min = cms.double(44.5),
      x_max = cms.double(49)
    ),
    rp_L_N = cms.PSet(
      x_min = cms.double(6.7),
      x_max = cms.double(11)
    ),
    rp_R_N = cms.PSet(
      x_min = cms.double(5.9),
      x_max = cms.double(10)
    ),
    rp_R_F = cms.PSet(
      x_min = cms.double(44.5),
      x_max = cms.double(49)
    ),
    mode_graph_min_N = cms.uint32(5),
    mult_sel_proj_y_min_entries = cms.uint32(300)
  ),
  binning = cms.PSet(
    bin_size_x = cms.double(0.1423314),
    n_bins_x = cms.uint32(210),
    pixel_x_offset = cms.double(40),
    n_bins_y = cms.uint32(400),
    y_min = cms.double(-20),
    y_max = cms.double(20)
  ),
  appendToDataLabel = cms.string('')
)
