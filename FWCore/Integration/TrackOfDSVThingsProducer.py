import FWCore.ParameterSet.Config as cms

def TrackOfDSVThingsProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackOfDSVThingsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
