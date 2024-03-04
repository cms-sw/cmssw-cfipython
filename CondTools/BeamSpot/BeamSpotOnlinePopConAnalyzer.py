import FWCore.ParameterSet.Config as cms

def BeamSpotOnlinePopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlinePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
