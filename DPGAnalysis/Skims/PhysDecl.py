import FWCore.ParameterSet.Config as cms

def PhysDecl(*args, **kwargs):
  mod = cms.EDFilter('PhysDecl',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
