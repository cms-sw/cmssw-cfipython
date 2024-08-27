import FWCore.ParameterSet.Config as cms

def TrackColMerger(**kwargs):
  mod = cms.EDProducer('TrackColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
