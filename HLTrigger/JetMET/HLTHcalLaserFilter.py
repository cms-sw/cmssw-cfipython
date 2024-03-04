import FWCore.ParameterSet.Config as cms

def HLTHcalLaserFilter(**kwargs):
  mod = cms.EDFilter('HLTHcalLaserFilter',
    hcalDigiCollection = cms.InputTag('hltHcalDigis'),
    maxTotalCalibCharge = cms.double(-1),
    timeSlices = cms.vint32(),
    thresholdsfC = cms.vdouble(),
    CalibCountFilterValues = cms.vint32(),
    CalibChargeFilterValues = cms.vdouble(),
    maxAllowedHFcalib = cms.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
