import FWCore.ParameterSet.Config as cms

def InputGenJetsParticleSelector(**kwargs):
  mod = cms.EDProducer('InputGenJetsParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
