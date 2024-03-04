import FWCore.ParameterSet.Config as cms

def CSCObjectMapESProducer(**kwargs):
  mod = cms.ESProducer('CSCObjectMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
