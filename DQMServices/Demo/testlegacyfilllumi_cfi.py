import FWCore.ParameterSet.Config as cms

testlegacyfilllumi = cms.EDAnalyzer('TestLegacyFillLumiEDAnalyzer',
  folder = cms.string('Legacy/testlegacyfilllumi'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
