import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryEPdd4hep(**kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryEPdd4hep',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
