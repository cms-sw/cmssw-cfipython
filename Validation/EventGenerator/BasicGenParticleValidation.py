import FWCore.ParameterSet.Config as cms

def BasicGenParticleValidation(**kwargs):
  mod = cms.EDProducer('BasicGenParticleValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
