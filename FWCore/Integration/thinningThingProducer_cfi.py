import FWCore.ParameterSet.Config as cms

thinningThingProducer = cms.EDProducer('ThinningThingProducer',
  inputTag = cms.required.InputTag,
  trackTag = cms.required.InputTag,
  offsetToThinnedKey = cms.required.uint32,
  expectedCollectionSize = cms.required.uint32,
  mightGet = cms.optional.untracked.vstring
)
