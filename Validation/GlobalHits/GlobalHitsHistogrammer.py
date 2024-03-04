import FWCore.ParameterSet.Config as cms

def GlobalHitsHistogrammer(**kwargs):
  mod = cms.EDProducer('GlobalHitsHistogrammer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
