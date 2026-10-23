import FWCore.ParameterSet.Config as cms

def GlobalDigisHistogrammer(*args, **kwargs):
  mod = cms.EDProducer('GlobalDigisHistogrammer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
