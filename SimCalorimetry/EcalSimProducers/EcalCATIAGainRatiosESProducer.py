import FWCore.ParameterSet.Config as cms

def EcalCATIAGainRatiosESProducer(**kwargs):
  mod = cms.ESProducer('EcalCATIAGainRatiosESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
