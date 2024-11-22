import FWCore.ParameterSet.Config as cms

def NegativeTrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('NegativeTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
