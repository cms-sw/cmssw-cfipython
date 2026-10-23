import FWCore.ParameterSet.Config as cms

def TestESSource(*args, **kwargs):
  mod = cms.ESSource('TestESSource',
    iterations = cms.uint32(10000000),
    checkIOVInitialization = cms.bool(False),
    expectedNumberOfConcurrentIOVs = cms.uint32(0),
    firstValidLumis = cms.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
