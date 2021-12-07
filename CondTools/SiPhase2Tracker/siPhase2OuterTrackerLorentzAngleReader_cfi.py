import FWCore.ParameterSet.Config as cms

siPhase2OuterTrackerLorentzAngleReader = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleReader',
  printDebug = cms.untracked.uint32(5),
  label = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
