import FWCore.ParameterSet.Config as cms

def IntProductFilter(**kwargs):
  mod = cms.EDFilter('IntProductFilter',
    label = cms.required.InputTag,
    threshold = cms.int32(0),
    shouldProduce = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
