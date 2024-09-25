import FWCore.ParameterSet.Config as cms

def WriteCTPPSPixGainCalibrations(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSPixGainCalibrations',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
