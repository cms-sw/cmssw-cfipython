import FWCore.ParameterSet.Config as cms

def BranchIDListsModifierProducer(*args, **kwargs):
  mod = cms.EDProducer('BranchIDListsModifierProducer',
    makeExtraProduct = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
