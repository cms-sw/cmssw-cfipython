import FWCore.ParameterSet.Config as cms

parameterSetBlobProducer = cms.EDProducer('ParameterSetBlobProducer',
  mightGet = cms.optional.untracked.vstring
)
