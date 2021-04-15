import FWCore.ParameterSet.Config as cms

randomEngineStateProducer = cms.EDProducer('RandomEngineStateProducer',
  mightGet = cms.optional.untracked.vstring
)
