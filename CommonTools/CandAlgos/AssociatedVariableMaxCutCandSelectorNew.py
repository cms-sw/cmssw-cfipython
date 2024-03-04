import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelectorNew(**kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelectorNew',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
