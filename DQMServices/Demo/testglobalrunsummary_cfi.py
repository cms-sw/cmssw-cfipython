import FWCore.ParameterSet.Config as cms

testglobalrunsummary = cms.EDProducer('TestDQMGlobalRunSummaryEDAnalyzer',
  folder = cms.string('Global/testglobal'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
