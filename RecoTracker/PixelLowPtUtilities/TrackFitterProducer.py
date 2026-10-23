import FWCore.ParameterSet.Config as cms

def TrackFitterProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackFitterProducer',
    TTRHBuilder = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
