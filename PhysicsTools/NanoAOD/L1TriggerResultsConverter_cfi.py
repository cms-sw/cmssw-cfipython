import FWCore.ParameterSet.Config as cms

L1TriggerResultsConverter = cms.EDProducer('L1TriggerResultsConverter',
  storeUnprefireableBit = cms.bool(False),
  src_ext = cms.InputTag('')
)
