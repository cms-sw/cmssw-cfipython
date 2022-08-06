import FWCore.ParameterSet.Config as cms

hcalFEDIntegrityTask = cms.EDProducer('HcalFEDIntegrityTask',
  name = cms.untracked.string('HcalFEDIntegrityTask'),
  debug = cms.untracked.int32(0),
  tagFEDs = cms.untracked.InputTag('rawDataCollector'),
  tagReport = cms.untracked.InputTag('hcalDigis'),
  MinHcalFEDID = cms.untracked.int32(1100),
  MaxHcalFEDID = cms.untracked.int32(1199),
  DirName = cms.untracked.string('Hcal/FEDIntegrity/'),
  mightGet = cms.optional.untracked.vstring
)