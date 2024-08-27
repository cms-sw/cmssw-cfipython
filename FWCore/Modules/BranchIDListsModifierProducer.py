import FWCore.ParameterSet.Config as cms

def BranchIDListsModifierProducer(**kwargs):
  mod = cms.EDProducer('BranchIDListsModifierProducer',
    makeExtraProduct = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
