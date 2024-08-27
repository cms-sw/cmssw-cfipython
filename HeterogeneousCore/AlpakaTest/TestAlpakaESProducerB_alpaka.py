import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerB_alpaka(**kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerB@alpaka',
    explicitLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
