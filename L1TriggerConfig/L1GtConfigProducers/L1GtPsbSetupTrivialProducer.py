import FWCore.ParameterSet.Config as cms

def L1GtPsbSetupTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtPsbSetupTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
