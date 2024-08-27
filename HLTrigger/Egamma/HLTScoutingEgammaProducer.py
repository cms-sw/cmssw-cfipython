import FWCore.ParameterSet.Config as cms

def HLTScoutingEgammaProducer(**kwargs):
  mod = cms.EDProducer('HLTScoutingEgammaProducer',
    EgammaCandidates = cms.InputTag('hltEgammaCandidates'),
    EgammaGsfTracks = cms.InputTag('hltEgammaGsfTracks'),
    SigmaIEtaIEtaMap = cms.InputTag('hltEgammaClusterShape', 'sigmaIEtaIEta5x5'),
    r9Map = cms.InputTag('hltEgammaR9ID', 'r95x5'),
    HoverEMap = cms.InputTag('hltEgammaHoverE'),
    DetaMap = cms.InputTag('hltEgammaGsfTrackVarsUnseeded', 'DetaSeed'),
    DphiMap = cms.InputTag('hltEgammaGsfTrackVarsUnseeded', 'Dphi'),
    MissingHitsMap = cms.InputTag('hltEgammaGsfTrackVarsUnseeded', 'MissingHits'),
    OneOEMinusOneOPMap = cms.InputTag('hltEgammaGsfTrackVarsUnseeded', 'OneOESuperMinusOneOP'),
    fBremMap = cms.InputTag('hltEgammaGsfTrackVarsUnseeded', 'fbrem'),
    EcalPFClusterIsoMap = cms.InputTag('hltEgammaEcalPFClusterIso'),
    EleGsfTrackIsoMap = cms.InputTag('hltEgammaEleGsfTrackIso'),
    HcalPFClusterIsoMap = cms.InputTag('hltEgammaHcalPFClusterIso'),
    egammaPtCut = cms.double(4),
    egammaEtaCut = cms.double(2.5),
    egammaHoverECut = cms.double(1),
    egammaSigmaIEtaIEtaCut = cms.vdouble(
      99999,
      99999
    ),
    absEtaBinUpperEdges = cms.vdouble(
      1.479,
      5
    ),
    saveRecHitTiming = cms.bool(False),
    mantissaPrecision = cms.int32(10),
    rechitMatrixSize = cms.int32(10),
    rechitZeroSuppression = cms.bool(True),
    ecalRechitEB = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
    ecalRechitEE = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
