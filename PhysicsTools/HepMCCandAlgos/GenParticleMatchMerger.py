import FWCore.ParameterSet.Config as cms

def GenParticleMatchMerger(**kwargs):
  mod = cms.EDProducer('GenParticleMatchMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
