import FWCore.ParameterSet.Config as cms

def OnlineBeamSpotFromDB(*args, **kwargs):
  mod = cms.EDAnalyzer('OnlineBeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
