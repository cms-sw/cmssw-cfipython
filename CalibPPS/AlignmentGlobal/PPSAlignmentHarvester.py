import FWCore.ParameterSet.Config as cms

def PPSAlignmentHarvester(**kwargs):
  mod = cms.EDProducer('PPSAlignmentHarvester',
    dqm_dir = cms.string('AlCaReco/PPSAlignment'),
    sequence = cms.vstring(
      'x_alignment',
      'x_alignment_relative',
      'y_alignment'
    ),
    overwrite_sh_x = cms.bool(True),
    text_results_path = cms.string('./alignment_results.txt'),
    write_sqlite_results = cms.bool(False),
    x_ali_rel_final_slope_fixed = cms.bool(False),
    y_ali_final_slope_fixed = cms.bool(False),
    x_corr_min = cms.double(-1000000),
    x_corr_max = cms.double(1000000),
    y_corr_min = cms.double(-1000000),
    y_corr_max = cms.double(1000000),
    detector_id = cms.uint32(7),
    subdetector_id = cms.uint32(4),
    debug = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod