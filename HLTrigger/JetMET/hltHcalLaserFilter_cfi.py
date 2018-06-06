import FWCore.ParameterSet.Config as cms

hltHcalLaserFilter = cms.EDFilter('HLTHcalLaserFilter',
  hcalDigiCollection = cms.InputTag('hltHcalDigis'),
  maxTotalCalibCharge = cms.double(-1),
  timeSlices = cms.vint32(),
  thresholdsfC = cms.vdouble(),
  CalibCountFilterValues = cms.vint32(),
  CalibChargeFilterValues = cms.vdouble(),
  maxAllowedHFcalib = cms.int32(-1)
)
