import FWCore.ParameterSet.Config as cms

hltJetsCleanedFromLeadingLeptonsRecoPFJet = cms.EDProducer('HLTPFJetsCleanedFromLeadingLeptons',
  leptons = cms.InputTag('triggerFilterObjectWithRefs'),
  jets = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.3),
  numLeptons = cms.uint32(1)
)
