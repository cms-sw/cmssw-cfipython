import FWCore.ParameterSet.Config as cms

def StraightLinePropagatorESProducer(**kwargs):
  mod = cms.ESProducer('StraightLinePropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
