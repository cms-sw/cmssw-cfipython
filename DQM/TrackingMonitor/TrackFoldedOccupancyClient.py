import FWCore.ParameterSet.Config as cms

def TrackFoldedOccupancyClient(*args, **kwargs):
  mod = cms.EDProducer('TrackFoldedOccupancyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
