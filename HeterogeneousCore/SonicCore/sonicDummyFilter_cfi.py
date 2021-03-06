import FWCore.ParameterSet.Config as cms

sonicDummyFilter = cms.EDFilter('SonicDummyFilter',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    factor = cms.int32(-1),
    wait = cms.int32(10),
    fails = cms.uint32(0)
  ),
  input = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
