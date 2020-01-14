import FWCore.ParameterSet.Config as cms

testglobal = cms.EDProducer('TestDQMGlobalEDAnalyzer',
  folder = cms.string('Global/testglobal'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
