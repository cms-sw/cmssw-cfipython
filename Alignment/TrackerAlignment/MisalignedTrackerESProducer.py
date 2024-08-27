import FWCore.ParameterSet.Config as cms

def MisalignedTrackerESProducer(**kwargs):
  mod = cms.ESProducer('MisalignedTrackerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
