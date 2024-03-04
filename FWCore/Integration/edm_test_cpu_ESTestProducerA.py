import FWCore.ParameterSet.Config as cms

def edm_test_cpu_ESTestProducerA(**kwargs):
  mod = cms.ESProducer('edm::test::cpu::ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
