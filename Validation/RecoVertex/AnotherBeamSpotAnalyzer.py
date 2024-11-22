import FWCore.ParameterSet.Config as cms

def AnotherBeamSpotAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('AnotherBeamSpotAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
