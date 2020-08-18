import FWCore.ParameterSet.Config as cms

hgcalSimHitValidationEE = cms.EDProducer('HGCalSimHitValidation',
  DetectorName = cms.string('HGCalEESensitive'),
  CaloHitSource = cms.string('HGCHitsEE'),
  TimeSlices = cms.vdouble(
    25,
    1000
  ),
  Verbosity = cms.untracked.int32(0),
  TestNumber = cms.untracked.bool(True),
  fromDDD = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
