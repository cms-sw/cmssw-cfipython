import FWCore.ParameterSet.Config as cms

def GenJetParticleRefSelector(*args, **kwargs):
  mod = cms.EDFilter('GenJetParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
