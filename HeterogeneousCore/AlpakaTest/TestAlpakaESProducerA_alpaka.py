import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerA_alpaka(**kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerA@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
