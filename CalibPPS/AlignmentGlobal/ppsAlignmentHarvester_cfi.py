import FWCore.ParameterSet.Config as cms

ppsAlignmentHarvester = cms.EDProducer('PPSAlignmentHarvester',
  dqm_dir = cms.string('AlCaReco/PPSAlignment'),
  sequence = cms.vstring(
    'x_alignment',
    'x_alignment_relative',
    'y_alignment'
  ),
  overwrite_sh_x = cms.bool(True),
  text_results_path = cms.string('./alignment_results.txt'),
  write_sqlite_results = cms.bool(False),
  x_ali_rel_final_slope_fixed = cms.bool(True),
  y_ali_final_slope_fixed = cms.bool(True),
  x_corr_min = cms.double(-1000000),
  x_corr_max = cms.double(1000000),
  y_corr_min = cms.double(-1000000),
  y_corr_max = cms.double(1000000),
  debug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
