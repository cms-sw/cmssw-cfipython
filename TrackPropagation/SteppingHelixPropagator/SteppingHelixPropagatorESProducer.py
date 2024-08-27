import FWCore.ParameterSet.Config as cms

def SteppingHelixPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('SteppingHelixPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
