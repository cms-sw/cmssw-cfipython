import FWCore.ParameterSet.Config as cms

def edm_test_other_ESTestProducerA(**kwargs):
  mod = cms.ESProducer('edm::test::other::ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
