import FWCore.ParameterSet.Config as cms

def ThinningDSVThingProducer(*args, **kwargs):
  mod = cms.EDProducer('ThinningDSVThingProducer',
    inputTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    offsetToValue = cms.uint32(0),
    expectedDetSets = cms.required.uint32,
    expectedDetSetSize = cms.required.uint32,
    slimmedValueFactor = cms.int32(1),
    thinnedRefSetIgnoreInvalidParentRef = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
