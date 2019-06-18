import FWCore.ParameterSet.Config as cms

UnclusteredBlobProducer = cms.EDProducer('UnclusteredBlobProducer',
  candsrc = cms.InputTag('badUnclustered'),
  mightGet = cms.optional.untracked.vstring
)
