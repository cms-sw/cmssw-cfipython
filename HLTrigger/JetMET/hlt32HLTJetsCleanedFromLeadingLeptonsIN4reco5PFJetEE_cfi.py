import FWCore.ParameterSet.Config as cms

hlt32HLTJetsCleanedFromLeadingLeptonsIN4reco5PFJetEE = cms.EDProducer('HLTPFJetsCleanedFromLeadingLeptons',
  leptons = cms.InputTag('triggerFilterObjectWithRefs'),
  jets = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.3),
  numLeptons = cms.uint32(1)
)
