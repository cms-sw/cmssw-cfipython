import FWCore.ParameterSet.Config as cms

def TruthGraphMixedProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthGraphMixedProducer',
    simTracks = cms.InputTag('mix', 'g4SimHits'),
    simVertices = cms.InputTag('mix', 'g4SimHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
