import FWCore.ParameterSet.Config as cms

PFJetsMaxInvMassModule = cms.EDProducer('PFJetsMaxInvMassModule',
  PFJetSrc = cms.InputTag(''),
  maxInvMassPairOnly = cms.bool(True),
  removeMaxInvMassPair = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
