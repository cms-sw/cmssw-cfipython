import FWCore.ParameterSet.Config as cms

def NegativeTrackCountingESProducer(**kwargs):
  mod = cms.ESProducer('NegativeTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
