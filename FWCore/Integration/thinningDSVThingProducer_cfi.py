import FWCore.ParameterSet.Config as cms

thinningDSVThingProducer = cms.EDProducer('ThinningDSVThingProducer',
  inputTag = cms.required.InputTag,
  trackTag = cms.required.InputTag,
  offsetToValue = cms.uint32(0),
  expectedDetSets = cms.required.uint32,
  expectedDetSetSize = cms.required.uint32,
  slimmedValueFactor = cms.int32(1),
  thinnedRefSetIgnoreInvalidParentRef = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
