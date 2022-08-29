import FWCore.ParameterSet.Config as cms

siPhase2OTFakeLorentzAngleESSource = cms.ESSource('SiPhase2OuterTrackerFakeLorentzAngleESSource',
  LAValue = cms.double(0.07),
  recordName = cms.string('LorentzAngle'),
  appendToDataLabel = cms.string('')
)
