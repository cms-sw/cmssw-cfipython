import FWCore.ParameterSet.Config as cms

siPhase2OuterTrackerLorentzAngleWriter = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleWriter',
  record = cms.string('SiPhase2OuterTrackerLorentzAngleRcd'),
  tag = cms.string('SiPhase2OuterTrackerLorentzAngle'),
  value = cms.double(0.07),
  mightGet = cms.optional.untracked.vstring
)
