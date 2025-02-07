import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandRefSelector(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandRefSelector',
    src = cms.InputTag(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
