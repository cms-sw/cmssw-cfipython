import FWCore.ParameterSet.Config as cms

def TrajectoryCleanerESProducer(**kwargs):
  mod = cms.ESProducer('TrajectoryCleanerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
