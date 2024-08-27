import FWCore.ParameterSet.Config as cms

def VertexFromTrackProducer(**kwargs):
  mod = cms.EDProducer('VertexFromTrackProducer',
    isRecoCandidate = cms.bool(False),
    trackLabel = cms.InputTag('hltL3MuonCandidates'),
    useTriggerFilterElectrons = cms.bool(False),
    triggerFilterElectronsSrc = cms.InputTag('hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoL1JetTrackIsoFilter'),
    useTriggerFilterMuons = cms.bool(True),
    triggerFilterMuonsSrc = cms.InputTag('hltSingleMuIsoL3IsoFiltered15'),
    useBeamSpot = cms.bool(True),
    beamSpotLabel = cms.InputTag('hltOnlineBeamSpot'),
    useVertex = cms.bool(True),
    vertexLabel = cms.InputTag('hltPixelVertices'),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
