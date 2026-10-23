import FWCore.ParameterSet.Config as cms

def TrackAlgoCompareUtil(*args, **kwargs):
  mod = cms.EDProducer('TrackAlgoCompareUtil',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
