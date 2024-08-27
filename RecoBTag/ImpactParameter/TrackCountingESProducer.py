import FWCore.ParameterSet.Config as cms

def TrackCountingESProducer(**kwargs):
  mod = cms.ESProducer('TrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
