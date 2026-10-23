import FWCore.ParameterSet.Config as cms

def CTPPSPixGainCalibsESAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSPixGainCalibsESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
