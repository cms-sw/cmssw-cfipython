import FWCore.ParameterSet.Config as cms

testone = cms.EDProducer('TestDQMOneEDAnalyzer',
  folder = cms.string('One/testone'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
