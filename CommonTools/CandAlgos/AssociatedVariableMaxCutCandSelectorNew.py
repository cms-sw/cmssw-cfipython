import FWCore.ParameterSet.Config as cms

def AssociatedVariableMaxCutCandSelectorNew(*args, **kwargs):
  mod = cms.EDFilter('AssociatedVariableMaxCutCandSelectorNew',
    src = cms.InputTag(''),
    var = cms.InputTag(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
