import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerBlocks_alpaka(*args, **kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerBlocks@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
