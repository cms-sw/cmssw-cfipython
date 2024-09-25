import FWCore.ParameterSet.Config as cms

def ConcurrentIOVESSource(*args, **kwargs):
  mod = cms.ESSource('ConcurrentIOVESSource',
    iovIsRunNotTime = cms.bool(True),
    concurrentFinder = cms.bool(True),
    testForceESSourceMode = cms.bool(False),
    findForRecordA = cms.bool(False),
    firstValidLumis = cms.vuint32(),
    invalidLumis = cms.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
