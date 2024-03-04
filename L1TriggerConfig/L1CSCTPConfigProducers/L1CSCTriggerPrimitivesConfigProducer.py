import FWCore.ParameterSet.Config as cms

def L1CSCTriggerPrimitivesConfigProducer(**kwargs):
  mod = cms.ESProducer('L1CSCTriggerPrimitivesConfigProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
