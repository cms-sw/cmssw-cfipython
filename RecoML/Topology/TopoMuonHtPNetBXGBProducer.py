import FWCore.ParameterSet.Config as cms

def TopoMuonHtPNetBXGBProducer(*args, **kwargs):
  mod = cms.EDProducer('TopoMuonHtPNetBXGBProducer',
    PFHT = cms.InputTag('hltPFHTJet30'),
    PNetBscore = cms.InputTag('hltParticleNetDiscriminatorsJetTags', 'BvsAll'),
    ChargedCandidates = cms.InputTag('hltIterL3MuonCandidates'),
    EcalPFClusterIsoMap = cms.InputTag('hltMuonEcalMFPFClusterIsoForMuons'),
    HcalPFClusterIsoMap = cms.InputTag('hltMuonHcalRegPFClusterIsoForMuons'),
    TrackIsoMap = cms.InputTag('hltMuonTkRelIsolationCut0p3Map', 'combinedRelativeIsoDeposits'),
    modelPath = cms.FileInPath('HLTrigger/HLTfilters/data/HLT_xgb_model_HH2b2W1L_1mu_HLTHT_sorttkisoMupt-absiso_PNetB.json'),
    nMuons = cms.uint32(1),
    nPNetB = cms.uint32(1),
    muonPtCut = cms.double(10),
    muonEtaCut = cms.double(2.4),
    muonSortByTkIso = cms.bool(True),
    nTreeLimit = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
