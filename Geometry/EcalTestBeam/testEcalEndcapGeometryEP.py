import FWCore.ParameterSet.Config as cms

def testEcalEndcapGeometryEP(**kwargs):
  mod = cms.ESProducer('testEcalEndcapGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
