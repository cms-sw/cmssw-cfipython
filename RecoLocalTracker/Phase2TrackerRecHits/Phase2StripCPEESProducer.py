import FWCore.ParameterSet.Config as cms

def Phase2StripCPEESProducer(**kwargs):
  mod = cms.ESProducer('Phase2StripCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
