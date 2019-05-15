import FWCore.ParameterSet.Config as cms

hltScoutingEgammaProducer = cms.EDProducer('HLTScoutingEgammaProducer',
  EgammaCandidates = cms.InputTag('hltEgammaCandidates'),
  EgammaGsfTracks = cms.InputTag('hltEgammaGsfTracks'),
  SigmaIEtaIEtaMap = cms.InputTag('hltEgammaClusterShape', 'sigmaIEtaIEta5x5'),
  HoverEMap = cms.InputTag('hltEgammaHoverE'),
  DetaMap = cms.InputTag('hltEgammaGsfTrackVars', 'Deta'),
  DphiMap = cms.InputTag('hltEgammaGsfTrackVars', 'Dphi'),
  MissingHitsMap = cms.InputTag('hltEgammaGsfTrackVars', 'MissingHits'),
  OneOEMinusOneOPMap = cms.InputTag('hltEgammaGsfTrackVars', 'OneOESuperMinusOneOP'),
  EcalPFClusterIsoMap = cms.InputTag('hltEgammaEcalPFClusterIso'),
  EleGsfTrackIsoMap = cms.InputTag('hltEgammaEleGsfTrackIso'),
  HcalPFClusterIsoMap = cms.InputTag('hltEgammaHcalPFClusterIso'),
  egammaPtCut = cms.double(4),
  egammaEtaCut = cms.double(2.5),
  egammaHoverECut = cms.double(1)
)
