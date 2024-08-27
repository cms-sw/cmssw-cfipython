import FWCore.ParameterSet.Config as cms

def DIPLumiProducer(**kwargs):
  mod = cms.ESSource('DIPLumiProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
