import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerD_alpaka(**kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerD@alpaka',
    srcA = cms.ESInputTag('', ''),
    srcB = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
