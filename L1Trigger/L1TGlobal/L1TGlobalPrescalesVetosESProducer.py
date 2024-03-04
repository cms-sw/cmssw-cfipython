import FWCore.ParameterSet.Config as cms

def L1TGlobalPrescalesVetosESProducer(**kwargs):
  mod = cms.ESProducer('L1TGlobalPrescalesVetosESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
