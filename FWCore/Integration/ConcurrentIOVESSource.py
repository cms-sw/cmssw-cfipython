import FWCore.ParameterSet.Config as cms

def ConcurrentIOVESSource(**kwargs):
  mod = cms.ESSource('ConcurrentIOVESSource',
    iovIsRunNotTime = cms.bool(True),
    concurrentFinder = cms.bool(True),
    testForceESSourceMode = cms.bool(False),
    findForRecordA = cms.bool(False),
    firstValidLumis = cms.vuint32(),
    invalidLumis = cms.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
