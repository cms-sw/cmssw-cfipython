import FWCore.ParameterSet.Config as cms

def TrackAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
