import FWCore.ParameterSet.Config as cms

def GenPlusSimParticleProducer(**kwargs):
  mod = cms.EDProducer('GenPlusSimParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
