import FWCore.ParameterSet.Config as cms

HLTDummyCollections = cms.EDProducer('HLTDummyCollections',
  action = cms.string(''),
  UnpackZDC = cms.bool(False),
  ESdigiCollection = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
