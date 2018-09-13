import FWCore.ParameterSet.Config as cms

bunchSpacingProducer = cms.EDProducer('BunchSpacingProducer',
  overrideBunchSpacing = cms.bool(False),
  bunchSpacingOverride = cms.uint32(25)
)
