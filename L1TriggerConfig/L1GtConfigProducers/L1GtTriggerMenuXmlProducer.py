import FWCore.ParameterSet.Config as cms

def L1GtTriggerMenuXmlProducer(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMenuXmlProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
