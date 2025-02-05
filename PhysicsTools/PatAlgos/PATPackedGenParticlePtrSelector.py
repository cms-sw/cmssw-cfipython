import FWCore.ParameterSet.Config as cms

def PATPackedGenParticlePtrSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPackedGenParticlePtrSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
