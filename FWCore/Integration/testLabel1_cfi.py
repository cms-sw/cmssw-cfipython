import FWCore.ParameterSet.Config as cms

testLabel1 = cms.EDProducer('ProducerWithPSetDesc',
  p_int = cms.int32(1),
  noDefaultPset1 = cms.PSet(),
  noDefaultPset2 = cms.PSet()
)
