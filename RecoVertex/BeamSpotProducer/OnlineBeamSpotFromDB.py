import FWCore.ParameterSet.Config as cms

def OnlineBeamSpotFromDB(**kwargs):
  mod = cms.EDAnalyzer('OnlineBeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
