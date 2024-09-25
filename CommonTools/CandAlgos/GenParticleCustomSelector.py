import FWCore.ParameterSet.Config as cms

def GenParticleCustomSelector(*args, **kwargs):
  mod = cms.EDFilter('GenParticleCustomSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
