import FWCore.ParameterSet.Config as cms

testlegacy = cms.EDAnalyzer('TestLegacyEDAnalyzer',
  folder = cms.string('Legacy/testlegacy'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
