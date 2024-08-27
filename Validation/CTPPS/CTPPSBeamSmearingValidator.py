import FWCore.ParameterSet.Config as cms

def CTPPSBeamSmearingValidator(**kwargs):
  mod = cms.EDAnalyzer('CTPPSBeamSmearingValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
