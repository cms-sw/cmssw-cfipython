import FWCore.ParameterSet.Config as cms

def HLTDynamicPrescaler(**kwargs):
  mod = cms.EDFilter('HLTDynamicPrescaler',
    saveTags = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
