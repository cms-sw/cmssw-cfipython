import FWCore.ParameterSet.Config as cms

def IntProductFilter(*args, **kwargs):
  mod = cms.EDFilter('IntProductFilter',
    label = cms.required.InputTag,
    threshold = cms.int32(0),
    shouldProduce = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
