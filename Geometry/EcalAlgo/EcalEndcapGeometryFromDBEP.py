import FWCore.ParameterSet.Config as cms

def EcalEndcapGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('EcalEndcapGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
