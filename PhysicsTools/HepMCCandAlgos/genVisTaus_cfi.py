import FWCore.ParameterSet.Config as cms

genVisTaus = cms.EDProducer('GenVisTauProducer',
  src = cms.required.InputTag,
  srcGenParticles = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
