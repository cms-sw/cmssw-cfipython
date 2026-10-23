import FWCore.ParameterSet.Config as cms

def edm_test_other_ESTestProducerA(*args, **kwargs):
  mod = cms.ESProducer('edm::test::other::ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
