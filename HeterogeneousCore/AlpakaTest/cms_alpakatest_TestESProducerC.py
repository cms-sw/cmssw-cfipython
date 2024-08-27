import FWCore.ParameterSet.Config as cms

def cms_alpakatest_TestESProducerC(**kwargs):
  mod = cms.ESProducer('cms::alpakatest::TestESProducerC',
    value = cms.required.int32,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
