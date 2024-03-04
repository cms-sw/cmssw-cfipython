import FWCore.ParameterSet.Config as cms

def FFTPFJetSysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
