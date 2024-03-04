import FWCore.ParameterSet.Config as cms

def TrackListMerger(**kwargs):
  mod = cms.EDProducer('TrackListMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
