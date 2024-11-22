import FWCore.ParameterSet.Config as cms

def TrackDeepNNTagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackDeepNNTagInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
