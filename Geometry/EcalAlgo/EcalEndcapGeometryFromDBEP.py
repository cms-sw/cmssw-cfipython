import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
