import FWCore.ParameterSet.Config as cms

testonefillrun = cms.EDProducer('TestDQMOneFillRunEDAnalyzer',
  folder = cms.string('One/testonefillrun'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
