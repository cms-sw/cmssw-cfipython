import FWCore.ParameterSet.Config as cms

def LHEIntermediateParticlePtFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEIntermediateParticlePtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
