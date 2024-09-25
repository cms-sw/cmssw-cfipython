import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelector(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
