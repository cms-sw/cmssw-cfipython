import FWCore.ParameterSet.Config as cms

def LHEIntermediateParticlePtFilter(**kwargs):
  mod = cms.EDFilter('LHEIntermediateParticlePtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
