import FWCore.ParameterSet.Config as cms

def PhysDecl(**kwargs):
  mod = cms.EDFilter('PhysDecl',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
