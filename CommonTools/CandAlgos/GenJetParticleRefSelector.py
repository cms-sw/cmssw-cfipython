import FWCore.ParameterSet.Config as cms

def GenJetParticleRefSelector(**kwargs):
  mod = cms.EDFilter('GenJetParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
