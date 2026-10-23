import FWCore.ParameterSet.Config as cms

def MCMultiParticleMassFilter(*args, **kwargs):
  mod = cms.EDFilter('MCMultiParticleMassFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
