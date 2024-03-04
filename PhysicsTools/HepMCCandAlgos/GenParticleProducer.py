import FWCore.ParameterSet.Config as cms

def GenParticleProducer(**kwargs):
  mod = cms.EDProducer('GenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
