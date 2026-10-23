import FWCore.ParameterSet.Config as cms

def testEcalEndcapGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('testEcalEndcapGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
