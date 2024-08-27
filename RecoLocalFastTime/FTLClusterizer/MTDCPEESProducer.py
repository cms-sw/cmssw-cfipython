import FWCore.ParameterSet.Config as cms

def MTDCPEESProducer(**kwargs):
  mod = cms.ESProducer('MTDCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
