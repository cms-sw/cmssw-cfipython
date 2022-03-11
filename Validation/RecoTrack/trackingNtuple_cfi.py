import FWCore.ParameterSet.Config as cms

trackingNtuple = cms.EDAnalyzer('TrackingNtuple',
  seedTracks = cms.untracked.VInputTag(
    'seedTracksinitialStepSeeds',
    'seedTracksdetachedTripletStepSeeds',
    'seedTrackspixelPairStepSeeds',
    'seedTrackslowPtTripletStepSeeds',
    'seedTracksmixedTripletStepSeeds',
    'seedTrackspixelLessStepSeeds',
    'seedTrackstobTecStepSeeds',
    'seedTracksjetCoreRegionalStepSeeds',
    'seedTracksmuonSeededSeedsInOut',
    'seedTracksmuonSeededSeedsOutIn'
  ),
  trackCandidates = cms.untracked.VInputTag(
    'initialStepTrackCandidates',
    'detachedTripletStepTrackCandidates',
    'pixelPairStepTrackCandidates',
    'lowPtTripletStepTrackCandidates',
    'mixedTripletStepTrackCandidates',
    'pixelLessStepTrackCandidates',
    'tobTecStepTrackCandidates',
    'jetCoreRegionalStepTrackCandidates',
    'muonSeededTrackCandidatesInOut',
    'muonSeededTrackCandidatesOutIn'
  ),
  tracks = cms.untracked.InputTag('generalTracks'),
  trackMVAs = cms.untracked.vstring('generalTracks'),
  clusterMasks = cms.untracked.VPSet(
    cms.PSet(
      index = cms.untracked.uint32(24),
      src = cms.untracked.InputTag('detachedQuadStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(22),
      src = cms.untracked.InputTag('highPtTripletStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(7),
      src = cms.untracked.InputTag('detachedTripletStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(23),
      src = cms.untracked.InputTag('lowPtQuadStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(5),
      src = cms.untracked.InputTag('lowPtTripletStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(8),
      src = cms.untracked.InputTag('mixedTripletStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(9),
      src = cms.untracked.InputTag('pixelLessStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(6),
      src = cms.untracked.InputTag('pixelPairStepClusters')
    ),
    cms.PSet(
      index = cms.untracked.uint32(10),
      src = cms.untracked.InputTag('tobTecStepClusters')
    )
  ),
  trackingParticles = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
  trackingParticlesRef = cms.untracked.bool(False),
  clusterTPMap = cms.untracked.InputTag('tpClusterProducer'),
  simHitTPMap = cms.untracked.InputTag('simHitTPAssocProducer'),
  trackAssociator = cms.untracked.InputTag('quickTrackAssociatorByHits'),
  pixelDigiSimLink = cms.untracked.InputTag('simSiPixelDigis'),
  stripDigiSimLink = cms.untracked.InputTag('simSiStripDigis'),
  phase2OTSimLink = cms.untracked.InputTag(''),
  beamSpot = cms.untracked.InputTag('offlineBeamSpot'),
  pixelRecHits = cms.untracked.InputTag('siPixelRecHits'),
  stripRphiRecHits = cms.untracked.InputTag('siStripMatchedRecHits', 'rphiRecHit'),
  stripStereoRecHits = cms.untracked.InputTag('siStripMatchedRecHits', 'stereoRecHit'),
  stripMatchedRecHits = cms.untracked.InputTag('siStripMatchedRecHits', 'matchedRecHit'),
  phase2OTRecHits = cms.untracked.InputTag('siPhase2RecHits'),
  vertices = cms.untracked.InputTag('offlinePrimaryVertices'),
  trackingVertices = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
  trackingParticleNlayers = cms.untracked.InputTag('trackingParticleNumberOfLayersProducer', 'trackerLayers'),
  trackingParticleNpixellayers = cms.untracked.InputTag('trackingParticleNumberOfLayersProducer', 'pixelLayers'),
  trackingParticleNstripstereolayers = cms.untracked.InputTag('trackingParticleNumberOfLayersProducer', 'stripStereoLayers'),
  TTRHBuilder = cms.untracked.string('WithTrackAngle'),
  includeSeeds = cms.untracked.bool(False),
  addSeedCurvCov = cms.untracked.bool(False),
  includeAllHits = cms.untracked.bool(False),
  includeMVA = cms.untracked.bool(True),
  includeTrackingParticles = cms.untracked.bool(True),
  includeOOT = cms.untracked.bool(False),
  keepEleSimHits = cms.untracked.bool(False),
  saveSimHitsP3 = cms.untracked.bool(False),
  simHitBySignificance = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
