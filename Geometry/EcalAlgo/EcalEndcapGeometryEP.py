import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
