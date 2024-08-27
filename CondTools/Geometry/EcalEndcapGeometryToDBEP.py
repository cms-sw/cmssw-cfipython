import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
