import FWCore.ParameterSet.Config as cms

hltCaloJetHFCleaner = cms.EDProducer('HLTCaloJetHFCleaner',
  jets = cms.InputTag('hltAK4PFJetsTightIDCorrected'),
  mets = cms.InputTag('hltMet'),
  sigmaEtaEta = cms.InputTag('hltHFJetShowerShape', 'sigmaEtaEta'),
  sigmaPhiPhi = cms.InputTag('hltHFJetShowerShape', 'sigmaPhiPhi'),
  centralEtaStripSize = cms.InputTag('hltHFJetShowerShape', 'centralEtaStripSize'),
  jetPtMin = cms.double(100),
  dphiJetMetMin = cms.double(2.5),
  jetEtaMin = cms.double(2.9),
  jetEtaMax = cms.double(5),
  sigmaEtaPhiDiffMax = cms.double(0.05),
  cornerCutSigmaEtaEta = cms.double(0.02),
  cornerCutSigmaPhiPhi = cms.double(0.02),
  centralEtaStripSizeMax = cms.int32(2),
  applySigmaEtaPhiCornerCut = cms.bool(True),
  applySigmaEtaPhiCut = cms.bool(True),
  applyStripSizeCut = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
