import FWCore.ParameterSet.Config as cms

def LSTModulesDevESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('LSTModulesDevESProducer@alpaka',
    ptCut = cms.double(0.8),
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
