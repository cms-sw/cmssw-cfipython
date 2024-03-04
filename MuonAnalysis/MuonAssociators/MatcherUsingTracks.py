import FWCore.ParameterSet.Config as cms

def MatcherUsingTracks(**kwargs):
  mod = cms.EDProducer('MatcherUsingTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
