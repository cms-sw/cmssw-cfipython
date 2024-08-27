import FWCore.ParameterSet.Config as cms

def GenParticlePruner(**kwargs):
  mod = cms.EDProducer('GenParticlePruner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
