import FWCore.ParameterSet.Config as cms

RecoTauPiZeroUnembedder = cms.EDProducer('RecoTauPiZeroUnembedder',
  src = cms.InputTag('hpsPFTauProducerSansRefs'),
  mightGet = cms.optional.untracked.vstring
)
