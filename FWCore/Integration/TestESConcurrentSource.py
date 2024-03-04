import FWCore.ParameterSet.Config as cms

def TestESConcurrentSource(**kwargs):
  mod = cms.ESSource('TestESConcurrentSource',
    iterations = cms.uint32(10000000),
    checkIOVInitialization = cms.bool(False),
    expectedNumberOfConcurrentIOVs = cms.uint32(0),
    firstValidLumis = cms.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
