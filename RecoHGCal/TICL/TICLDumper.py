import FWCore.ParameterSet.Config as cms

def TICLDumper(**kwargs):
  mod = cms.EDAnalyzer('TICLDumper',
    trackstersclue3d = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    ticlcandidates = cms.InputTag('ticlTrackstersMerge'),
    tracks = cms.InputTag('generalTracks'),
    tracksTime = cms.InputTag('tofPID', 't0'),
    tracksTimeQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    tracksTimeErr = cms.InputTag('tofPID', 'sigmat0'),
    trackstersmerged = cms.InputTag('ticlTrackstersMerge'),
    simtrackstersSC = cms.InputTag('ticlSimTracksters'),
    simtrackstersCP = cms.InputTag('ticlSimTracksters', 'fromCPs'),
    simtrackstersPU = cms.InputTag('ticlSimTracksters', 'PU'),
    simTICLCandidates = cms.InputTag('ticlSimTracksters'),
    recoToSimAssociatorSC = cms.InputTag('tracksterSimTracksterAssociationPRbyCLUE3D', 'recoToSim'),
    simToRecoAssociatorSC = cms.InputTag('tracksterSimTracksterAssociationPRbyCLUE3D', 'simToReco'),
    recoToSimAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinkingbyCLUE3D', 'recoToSim'),
    simToRecoAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinkingbyCLUE3D', 'simToReco'),
    MergerecoToSimAssociatorSC = cms.InputTag('tracksterSimTracksterAssociationPR', 'recoToSim'),
    MergesimToRecoAssociatorSC = cms.InputTag('tracksterSimTracksterAssociationPR', 'simToReco'),
    MergerecoToSimAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinking', 'recoToSim'),
    MergesimToRecoAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinking', 'simToReco'),
    MergerecoToSimAssociatorPU = cms.InputTag('tracksterSimTracksterAssociationLinkingPU', 'recoToSim'),
    MergesimToRecoAssociatorPU = cms.InputTag('tracksterSimTracksterAssociationLinkingPU', 'simToReco'),
    simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
    caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    saveLCs = cms.bool(True),
    saveCLUE3DTracksters = cms.bool(True),
    saveTrackstersMerged = cms.bool(True),
    saveSimTrackstersSC = cms.bool(True),
    saveSimTrackstersCP = cms.bool(True),
    saveTICLCandidate = cms.bool(True),
    saveSimTICLCandidate = cms.bool(True),
    saveTracks = cms.bool(True),
    saveAssociations = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
