import FWCore.ParameterSet.Config as cms

pileupJetIDVarProducer = cms.EDProducer('PileupJetIDVarProducer',
  srcJet = cms.required.InputTag,
  srcPileupJetId = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
