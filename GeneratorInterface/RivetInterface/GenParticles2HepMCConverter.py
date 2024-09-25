import FWCore.ParameterSet.Config as cms

def GenParticles2HepMCConverter(*args, **kwargs):
  mod = cms.EDProducer('GenParticles2HepMCConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
