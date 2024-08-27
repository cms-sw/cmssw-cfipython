import FWCore.ParameterSet.Config as cms

def CSCIndexerESProducer(**kwargs):
  mod = cms.ESProducer('CSCIndexerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
