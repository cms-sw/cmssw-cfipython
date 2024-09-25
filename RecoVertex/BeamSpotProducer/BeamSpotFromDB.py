import FWCore.ParameterSet.Config as cms

def BeamSpotFromDB(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
