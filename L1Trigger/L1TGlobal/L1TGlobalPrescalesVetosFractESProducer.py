import FWCore.ParameterSet.Config as cms

def L1TGlobalPrescalesVetosFractESProducer(**kwargs):
  mod = cms.ESProducer('L1TGlobalPrescalesVetosFractESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
