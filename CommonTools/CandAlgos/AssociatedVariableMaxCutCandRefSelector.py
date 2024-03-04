import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandRefSelector(**kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
