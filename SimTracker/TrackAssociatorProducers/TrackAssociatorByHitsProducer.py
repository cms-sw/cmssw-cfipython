import FWCore.ParameterSet.Config as cms

def TrackAssociatorByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackAssociatorByHitsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
