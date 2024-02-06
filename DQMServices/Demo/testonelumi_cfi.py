import FWCore.ParameterSet.Config as cms

testonelumi = cms.EDProducer('TestDQMOneLumiEDAnalyzer',
  folder = cms.string('One/testonelumi'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
