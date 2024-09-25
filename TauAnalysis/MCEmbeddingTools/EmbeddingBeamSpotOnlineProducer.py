import FWCore.ParameterSet.Config as cms

def EmbeddingBeamSpotOnlineProducer(*args, **kwargs):
  mod = cms.EDProducer('EmbeddingBeamSpotOnlineProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
