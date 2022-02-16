import FWCore.ParameterSet.Config as cms

tppfTausOnPFJetsDeltaR = cms.EDProducer('TPPFTausOnPFJetsDeltaR',
  enable = cms.required.bool,
  deltaR = cms.required.double,
  name = cms.untracked.string('No Name'),
  topCollection = cms.required.InputTag,
  bottomCollection = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
