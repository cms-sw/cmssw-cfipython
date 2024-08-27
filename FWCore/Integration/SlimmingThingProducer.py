import FWCore.ParameterSet.Config as cms

def SlimmingThingProducer(**kwargs):
  mod = cms.EDProducer('SlimmingThingProducer',
    inputTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    offsetToThinnedKey = cms.required.uint32,
    offsetToValue = cms.uint32(0),
    expectedCollectionSize = cms.required.uint32,
    slimmedValueFactor = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
