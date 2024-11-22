import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandRefSelector(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
