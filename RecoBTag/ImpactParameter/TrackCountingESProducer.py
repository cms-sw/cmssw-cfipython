import FWCore.ParameterSet.Config as cms

def TrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
