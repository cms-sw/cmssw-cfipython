import FWCore.ParameterSet.Config as cms

def GenParticles2HepMCConverter(**kwargs):
  mod = cms.EDProducer('GenParticles2HepMCConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
