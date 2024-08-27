import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandViewSelector(**kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
