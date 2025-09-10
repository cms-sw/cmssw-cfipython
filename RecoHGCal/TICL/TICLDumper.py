import FWCore.ParameterSet.Config as cms

def TICLDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('TICLDumper',
    tracksterCollections = cms.required.VPSet,
    trackstersInCand = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    ticlcandidates = cms.InputTag('ticlTrackstersMerge'),
    tracks = cms.InputTag('generalTracks'),
    tracksTime = cms.InputTag('tofPID', 't0'),
    tracksTimeQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    tracksTimeErr = cms.InputTag('tofPID', 'sigmat0'),
    tracksBeta = cms.InputTag('trackExtenderWithMTD', 'generalTrackBeta'),
    tracksTimeMtd = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    tracksTimeMtdErr = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    tracksPosMtd = cms.InputTag('trackExtenderWithMTD', 'generalTrackmtdpos'),
    muons = cms.InputTag('muons1stStep'),
    superclustering = cms.InputTag('ticlTracksterLinksSuperclusteringDNN'),
    recoSuperClusters = cms.InputTag('particleFlowSuperClusterHGCal'),
    recoSuperClusters_sourceTracksterCollection = cms.InputTag('ticlTrackstersMerge'),
    simtrackstersSC = cms.InputTag('ticlSimTracksters'),
    simTICLCandidates = cms.InputTag('ticlSimTracksters'),
    associators = cms.required.VPSet,
    simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
    caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    saveLCs = cms.bool(True),
    saveTICLCandidate = cms.bool(True),
    saveSimTICLCandidate = cms.bool(True),
    saveTracks = cms.bool(True),
    saveSuperclustering = cms.bool(True),
    saveRecoSuperclusters = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
