import FWCore.ParameterSet.Config as cms

def GenParticleRefSelector(*args, **kwargs):
  mod = cms.EDFilter('GenParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
