import FWCore.ParameterSet.Config as cms

def DeDxCalibrationDbCreator(*args, **kwargs):
  mod = cms.EDAnalyzer('DeDxCalibrationDbCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
