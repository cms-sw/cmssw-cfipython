import FWCore.ParameterSet.Config as cms

def HiBadParticleCleaner(**kwargs):
  mod = cms.EDProducer('HiBadParticleCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
