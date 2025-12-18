import FWCore.ParameterSet.Config as cms

def ElectronCalibrationUniv(*args, **kwargs):
  mod = cms.EDAnalyzer('ElectronCalibrationUniv',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
