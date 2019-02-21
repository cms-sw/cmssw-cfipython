import FWCore.ParameterSet.Config as cms

jetTracksAssociationToTrackRefs = cms.EDProducer('JetTracksAssociationToTrackRefs',
  association = cms.InputTag('ak4JetTracksAssociatorAtVertexPF'),
  jets = cms.InputTag('ak4PFJetsCHS'),
  corrector = cms.InputTag('ak4PFL1FastL2L3Corrector'),
  correctedPtMin = cms.double(0)
)
