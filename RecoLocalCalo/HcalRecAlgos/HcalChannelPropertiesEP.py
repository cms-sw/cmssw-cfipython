import FWCore.ParameterSet.Config as cms

def HcalChannelPropertiesEP(**kwargs):
  mod = cms.ESProducer('HcalChannelPropertiesEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
