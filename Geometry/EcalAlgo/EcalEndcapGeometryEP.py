import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryEP(**kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
