import FWCore.ParameterSet.Config as cms

def SlimmingDSVThingProducer(*args, **kwargs):
  mod = cms.EDProducer('SlimmingDSVThingProducer',
    inputTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    offsetToThinnedKey = cms.required.uint32,
    offsetToValue = cms.uint32(0),
    expectedDetSets = cms.required.uint32,
    expectedDetSetSize = cms.required.uint32,
    slimmedValueFactor = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
