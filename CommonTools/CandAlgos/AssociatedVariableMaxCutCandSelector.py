import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelector(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelector',
    src = cms.InputTag(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
