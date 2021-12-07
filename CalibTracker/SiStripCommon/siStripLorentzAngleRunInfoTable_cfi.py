import FWCore.ParameterSet.Config as cms

siStripLorentzAngleRunInfoTable = cms.EDProducer('SiStripLorentzAngleRunInfoTableProducer',
  name = cms.string('Det'),
  magFieldName = cms.string('magField'),
  doc = cms.string('Run info for the Lorentz angle measurement'),
  mightGet = cms.optional.untracked.vstring
)
