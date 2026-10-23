import FWCore.ParameterSet.Config as cms

def TrackAssociatorByPositionProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackAssociatorByPositionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
