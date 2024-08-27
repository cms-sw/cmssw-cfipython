import FWCore.ParameterSet.Config as cms

def TrackAlgoPriorityOrderESProducer(**kwargs):
  mod = cms.ESProducer('TrackAlgoPriorityOrderESProducer',
    ComponentName = cms.string('trackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
