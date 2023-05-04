import FWCore.ParameterSet.Config as cms

simpleCandidateFlatTableProducer = cms.EDProducer('SimpleCandidateFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  singleton = cms.bool(False),
  cut = cms.string(''),
  maxLen = cms.optional.uint32,
  externalVariables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
