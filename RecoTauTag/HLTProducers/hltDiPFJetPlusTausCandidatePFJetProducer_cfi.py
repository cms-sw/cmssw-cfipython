import FWCore.ParameterSet.Config as cms

hltDiPFJetPlusTausCandidatePFJetProducer = cms.EDProducer('HLTDiPFJetPlusTausCandidatePFJetProducer',
  pfJetSrc = cms.InputTag('hltAK4PFJetsCorrected'),
  tauSrc = cms.InputTag('hltSinglePFTau20TrackPt1LooseChargedIsolationReg'),
  extraTauPtCut = cms.double(45),
  mjjMin = cms.double(500),
  dRmin = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
