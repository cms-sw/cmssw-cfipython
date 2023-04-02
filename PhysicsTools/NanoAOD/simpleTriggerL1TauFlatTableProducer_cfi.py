import FWCore.ParameterSet.Config as cms

simpleTriggerL1TauFlatTableProducer = cms.EDProducer('SimpleTriggerL1TauFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  cut = cms.string(''),
  maxLen = cms.optional.uint32,
  minBX = cms.int32(-2),
  maxBX = cms.int32(2),
  alwaysWriteBXValue = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
