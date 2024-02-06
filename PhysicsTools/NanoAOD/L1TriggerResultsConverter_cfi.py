import FWCore.ParameterSet.Config as cms

L1TriggerResultsConverter = cms.EDProducer('L1TriggerResultsConverter',
  legacyL1 = cms.required.bool,
  src = cms.required.InputTag,
  storeUnprefireableBits = cms.bool(False),
  src_ext = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
