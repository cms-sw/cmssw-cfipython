import FWCore.ParameterSet.Config as cms

PFJetsTauOverlapRemoval = cms.EDProducer('PFJetsTauOverlapRemoval',
  PFJetSrc = cms.InputTag('hltAK4PFJetsCorrected'),
  TauSrc = cms.InputTag('hltSinglePFTau20TrackPt1LooseChargedIsolationReg'),
  Min_dR = cms.double(0.5)
)
