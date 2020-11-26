import FWCore.ParameterSet.Config as cms

ecalSimulationParametersAnalyzerEB = cms.EDAnalyzer('EcalSimParametersAnalyzer',
  name = cms.untracked.string('EcalHitsEB'),
  mightGet = cms.optional.untracked.vstring
)
