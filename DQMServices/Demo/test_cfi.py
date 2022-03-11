import FWCore.ParameterSet.Config as cms

test = cms.EDProducer('TestDQMEDAnalyzer',
  folder = cms.string('Normal/test'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
