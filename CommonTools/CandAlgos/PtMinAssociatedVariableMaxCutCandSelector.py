import FWCore.ParameterSet.Config as cms

def PtMinAssociatedVariableMaxCutCandSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinAssociatedVariableMaxCutCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
