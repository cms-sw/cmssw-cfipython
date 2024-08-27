import FWCore.ParameterSet.Config as cms

def GlobalRecHitsHistogrammer(**kwargs):
  mod = cms.EDProducer('GlobalRecHitsHistogrammer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
