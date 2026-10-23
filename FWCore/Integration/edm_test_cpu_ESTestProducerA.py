import FWCore.ParameterSet.Config as cms

def edm_test_cpu_ESTestProducerA(*args, **kwargs):
  mod = cms.ESProducer('edm::test::cpu::ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
