import FWCore.ParameterSet.Config as cms

def DeDxCalibrationDbCreator(**kwargs):
  mod = cms.EDAnalyzer('DeDxCalibrationDbCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
