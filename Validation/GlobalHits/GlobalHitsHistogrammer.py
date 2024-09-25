import FWCore.ParameterSet.Config as cms

def GlobalHitsHistogrammer(*args, **kwargs):
  mod = cms.EDProducer('GlobalHitsHistogrammer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
