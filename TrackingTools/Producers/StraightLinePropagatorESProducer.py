import FWCore.ParameterSet.Config as cms

def StraightLinePropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('StraightLinePropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
