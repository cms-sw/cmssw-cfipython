import FWCore.ParameterSet.Config as cms

producerWithPSetDesc = cms.EDProducer('ProducerWithPSetDesc',
  p_int = cms.int32(3),
  mightGet = cms.optional.untracked.vstring
)
