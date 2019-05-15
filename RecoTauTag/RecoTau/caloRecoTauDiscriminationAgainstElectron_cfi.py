import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationAgainstElectron = cms.EDProducer('CaloRecoTauDiscriminationAgainstElectron',
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  leadTrack_HCAL3x3hitsEtSumOverPt_minvalue = cms.double(0.1),
  maxleadTrackHCAL3x3hottesthitDEta = cms.double(0.1),
  ApplyCut_maxleadTrackHCAL3x3hottesthitDEta = cms.bool(False),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  ApplyCut_leadTrackavoidsECALcrack = cms.bool(True)
)
