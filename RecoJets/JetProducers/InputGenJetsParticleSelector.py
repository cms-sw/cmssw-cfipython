import FWCore.ParameterSet.Config as cms

def InputGenJetsParticleSelector(*args, **kwargs):
  mod = cms.EDProducer('InputGenJetsParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
