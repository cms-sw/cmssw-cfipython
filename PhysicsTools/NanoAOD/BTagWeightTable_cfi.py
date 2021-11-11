import FWCore.ParameterSet.Config as cms

BTagWeightTable = cms.EDProducer('BTagSFProducer',
  validate = cms.untracked.bool(False)
)
