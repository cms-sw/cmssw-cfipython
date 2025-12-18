import FWCore.ParameterSet.Config as cms

def GenParticlePruner(*args, **kwargs):
  mod = cms.EDProducer('GenParticlePruner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
