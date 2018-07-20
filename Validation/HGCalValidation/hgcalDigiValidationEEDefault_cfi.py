import FWCore.ParameterSet.Config as cms

hgcalDigiValidationEEDefault = cms.EDProducer('HGCalDigiValidation',
  DetectorName = cms.string('HGCalEESensitive'),
  DigiSource = cms.InputTag('hgcalDigis', 'EE'),
  ifHCAL = cms.bool(False),
  Verbosity = cms.untracked.int32(0),
  SampleIndx = cms.untracked.int32(0)
)