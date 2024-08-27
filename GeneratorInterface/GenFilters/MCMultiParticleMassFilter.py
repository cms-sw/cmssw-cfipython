import FWCore.ParameterSet.Config as cms

def MCMultiParticleMassFilter(**kwargs):
  mod = cms.EDFilter('MCMultiParticleMassFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
