import FWCore.ParameterSet.Config as cms

def TrackFoldedOccupancyClient(**kwargs):
  mod = cms.EDProducer('TrackFoldedOccupancyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
