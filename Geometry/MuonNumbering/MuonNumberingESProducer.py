import FWCore.ParameterSet.Config as cms

def MuonNumberingESProducer(**kwargs):
  mod = cms.ESProducer('MuonNumberingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
