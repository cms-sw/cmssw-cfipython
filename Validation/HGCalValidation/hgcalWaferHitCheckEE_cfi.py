import FWCore.ParameterSet.Config as cms

hgcalWaferHitCheckEE = cms.EDAnalyzer('HGCalWaferHitCheck',
  detectorName = cms.string('HGCalEESensitive'),
  caloHitSource = cms.string('HGCHitsEE'),
  source = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
  inputType = cms.int32(1),
  verbosity = cms.untracked.int32(0),
  ifNose = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
