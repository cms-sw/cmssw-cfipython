import FWCore.ParameterSet.Config as cms

hltScoutingPrimaryVertexProducer = cms.EDProducer('HLTScoutingPrimaryVertexProducer',
  vertexCollection = cms.InputTag('hltPixelVertices'),
  mightGet = cms.optional.untracked.vstring
)
