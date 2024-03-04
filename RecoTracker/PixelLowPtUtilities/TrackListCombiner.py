import FWCore.ParameterSet.Config as cms

def TrackListCombiner(**kwargs):
  mod = cms.EDProducer('TrackListCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
