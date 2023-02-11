import FWCore.ParameterSet.Config as cms

testlegacyharvester = cms.EDAnalyzer('TestLegacyHarvester',
  folder = cms.string('LegacyHarvester/'),
  mightGet = cms.optional.untracked.vstring
)
