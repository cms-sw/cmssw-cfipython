import FWCore.ParameterSet.Config as cms

def CTPPSBeamSmearingValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSBeamSmearingValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
