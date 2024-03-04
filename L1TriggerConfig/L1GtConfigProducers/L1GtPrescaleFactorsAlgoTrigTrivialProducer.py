import FWCore.ParameterSet.Config as cms

def L1GtPrescaleFactorsAlgoTrigTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtPrescaleFactorsAlgoTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
