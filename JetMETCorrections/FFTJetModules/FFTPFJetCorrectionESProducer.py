import FWCore.ParameterSet.Config as cms

def FFTPFJetCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
