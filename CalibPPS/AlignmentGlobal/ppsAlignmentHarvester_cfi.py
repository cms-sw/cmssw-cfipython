import FWCore.ParameterSet.Config as cms

ppsAlignmentHarvester = cms.EDProducer('PPSAlignmentHarvester',
  folder = cms.string('CalibPPS/Common'),
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
  debug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
