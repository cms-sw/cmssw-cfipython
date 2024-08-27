import FWCore.ParameterSet.Config as cms

def JetTracksAssociationToTrackRefs(**kwargs):
  mod = cms.EDProducer('JetTracksAssociationToTrackRefs',
    association = cms.InputTag('ak4JetTracksAssociatorAtVertexPF'),
    jets = cms.InputTag('ak4PFJetsCHS'),
    corrector = cms.InputTag('ak4PFL1FastL2L3Corrector'),
    correctedPtMin = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
