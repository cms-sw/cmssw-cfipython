import FWCore.ParameterSet.Config as cms

hltScoutingPrimaryVertexProducer = cms.EDProducer('HLTScoutingPrimaryVertexProducer',
  vertexCollection = cms.InputTag('hltPixelVertices'),
  mantissaPrecision = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)
