import FWCore.ParameterSet.Config as cms

hltDiJetEtaTopologyFilterRecoCaloJet = cms.EDFilter('HLTDiCaloJetEtaTopologyFilter',
  saveTags = cms.bool(True),
  inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
  minPtAve = cms.double(0),
  atLeastOneJetAbovePT = cms.double(0),
  minPtTag = cms.double(50),
  minPtProbe = cms.double(50),
  minDphi = cms.double(-1),
  minTagEta = cms.double(-1),
  maxTagEta = cms.double(1.4),
  minProbeEta = cms.double(2.7),
  maxProbeEta = cms.double(5.5),
  applyAbsToTag = cms.bool(False),
  applyAbsToProbe = cms.bool(False),
  oppositeEta = cms.bool(False),
  triggerType = cms.int32(85)
)
