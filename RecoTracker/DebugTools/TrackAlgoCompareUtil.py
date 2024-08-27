import FWCore.ParameterSet.Config as cms

def TrackAlgoCompareUtil(**kwargs):
  mod = cms.EDProducer('TrackAlgoCompareUtil',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
