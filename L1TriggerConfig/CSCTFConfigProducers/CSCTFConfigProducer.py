import FWCore.ParameterSet.Config as cms

def CSCTFConfigProducer(**kwargs):
  mod = cms.ESProducer('CSCTFConfigProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
