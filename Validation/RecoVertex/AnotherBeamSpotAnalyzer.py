import FWCore.ParameterSet.Config as cms

def AnotherBeamSpotAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('AnotherBeamSpotAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
