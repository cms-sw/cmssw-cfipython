import FWCore.ParameterSet.Config as cms

def BeamSpotFromDB(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
