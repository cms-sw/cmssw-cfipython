import FWCore.ParameterSet.Config as cms

def DTVDriftSegmentCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTVDriftSegmentCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
