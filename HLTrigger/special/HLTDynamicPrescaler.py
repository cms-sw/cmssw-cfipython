import FWCore.ParameterSet.Config as cms

def HLTDynamicPrescaler(*args, **kwargs):
  mod = cms.EDFilter('HLTDynamicPrescaler',
    saveTags = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
