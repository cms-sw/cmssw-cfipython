import FWCore.ParameterSet.Config as cms

L1HLTJetsMatching = cms.EDProducer('L1HLTTauMatching',
  L1TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
  JetSrc = cms.InputTag('hltSelectedPFTausTrackPt1MediumIsolationReg'),
  EtMin = cms.double(0)
)
