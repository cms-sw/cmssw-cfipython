import FWCore.ParameterSet.Config as cms

def PhotonXGBoostProducer(**kwargs):
  mod = cms.EDProducer('PhotonXGBoostProducer',
    candTag = cms.InputTag('hltEgammaCandidatesUnseeded'),
    inputTagR9 = cms.InputTag('hltEgammaR9IDUnseeded', 'r95x5'),
    inputTagHoE = cms.InputTag('hltEgammaHoverEUnseeded'),
    inputTagSigmaiEtaiEta = cms.InputTag('hltEgammaClusterShapeUnseeded', 'sigmaIEtaIEta5x5NoiseCleaned'),
    inputTagE2x2 = cms.InputTag('hltEgammaClusterShapeUnseeded', 'e2x2'),
    inputTagIso = cms.InputTag('hltEgammaEcalPFClusterIsoUnseeded'),
    mvaFileXgbB = cms.FileInPath('RecoEgamma/PhotonIdentification/data/XGBoost/Photon_NTL_168_Barrel_v1.bin'),
    mvaFileXgbE = cms.FileInPath('RecoEgamma/PhotonIdentification/data/XGBoost/Photon_NTL_158_Endcap_v1.bin'),
    mvaNTreeLimitB = cms.uint32(168),
    mvaNTreeLimitE = cms.uint32(158),
    mvaThresholdEt = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
