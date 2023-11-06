import FWCore.ParameterSet.Config as cms

BunchSpacingProducer = cms.EDProducer('BunchSpacingProducer',
  overrideBunchSpacing = cms.bool(False),
  bunchSpacingOverride = cms.uint32(25),
  mightGet = cms.optional.untracked.vstring
)
