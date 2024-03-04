import FWCore.ParameterSet.Config as cms

def L1TGlobalPrescalesVetosOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TGlobalPrescalesVetosOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
