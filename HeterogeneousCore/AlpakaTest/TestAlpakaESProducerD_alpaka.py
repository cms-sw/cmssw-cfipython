import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerD_alpaka(*args, **kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerD@alpaka',
    srcA = cms.ESInputTag('', ''),
    srcB = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
