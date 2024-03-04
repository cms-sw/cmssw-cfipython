import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelector(**kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
