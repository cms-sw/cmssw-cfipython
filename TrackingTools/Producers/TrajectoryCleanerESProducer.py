import FWCore.ParameterSet.Config as cms

def TrajectoryCleanerESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrajectoryCleanerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
