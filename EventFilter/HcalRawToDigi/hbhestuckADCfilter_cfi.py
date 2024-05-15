import FWCore.ParameterSet.Config as cms

hbhestuckADCfilter = cms.EDFilter('HBHEstuckADCfilter',
  digiLabel = cms.InputTag('hcalDigis'),
  thresholdADC = cms.int32(100),
  writeList = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
