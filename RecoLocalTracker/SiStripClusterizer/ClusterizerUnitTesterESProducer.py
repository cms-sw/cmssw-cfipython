import FWCore.ParameterSet.Config as cms

def ClusterizerUnitTesterESProducer(**kwargs):
  mod = cms.ESProducer('ClusterizerUnitTesterESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
