import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelectorNew(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelectorNew',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
