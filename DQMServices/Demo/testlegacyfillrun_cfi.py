import FWCore.ParameterSet.Config as cms

testlegacyfillrun = cms.EDAnalyzer('TestLegacyFillRunEDAnalyzer',
  folder = cms.string('Legacy/testlegacyfillrun'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
