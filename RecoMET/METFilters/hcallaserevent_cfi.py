import FWCore.ParameterSet.Config as cms

hcallaserevent = cms.EDFilter('HcalLaserEventFilter',
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
