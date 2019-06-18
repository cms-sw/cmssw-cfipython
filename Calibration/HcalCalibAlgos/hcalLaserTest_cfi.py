import FWCore.ParameterSet.Config as cms

hcalLaserTest = cms.EDAnalyzer('HcalLaserTest',
  InputHBHE = cms.InputTag('source'),
  InputHF = cms.InputTag('source'),
  UMNioDigis = cms.InputTag('UMNioDigis'),
  minADCHBHE = cms.int32(10),
  minADCHF = cms.int32(10),
  minFracDiffHBHELaser = cms.double(0.3),
  minFracHFLaser = cms.double(0.3),
  testMode = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
