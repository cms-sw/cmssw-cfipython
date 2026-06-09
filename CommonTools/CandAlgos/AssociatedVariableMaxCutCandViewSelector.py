import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandViewSelector',
    src = cms.InputTag(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
