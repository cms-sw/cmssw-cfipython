import FWCore.ParameterSet.Config as cms

def HcalLaserEventFilter(*args, **kwargs):
  mod = cms.EDFilter('HcalLaserEventFilter',
    vetoByRunEventNumber = cms.bool(False),
    vetoByHBHEOccupancy = cms.bool(True),
    minOccupiedHBHE = cms.uint32(4000),
    vetoByLaserMonitor = cms.bool(True),
    minLaserMonitorCharge = cms.double(5000),
    debug = cms.bool(False),
    reverseFilter = cms.bool(False),
    taggingMode = cms.bool(False),
    forceUseRecHitCollection = cms.bool(False),
    forceUseHcalNoiseSummary = cms.bool(False),
    BadRunEventNumbers = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
