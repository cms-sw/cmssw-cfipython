import FWCore.ParameterSet.Config as cms

simPFProducer = cms.EDProducer('SimPFProducer',
  simClustersSrc = cms.InputTag('particleFlowClusterHGCal'),
  trackSrc = cms.InputTag('generalTracks'),
  associators = cms.VInputTag('quickTrackAssociatorByHits'),
  pfRecTrackSrc = cms.InputTag('hgcalTrackCollection', 'TracksInHGCal'),
  trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
  neutralEMThreshold = cms.double(0.25),
  caloParticlesSrc = cms.InputTag('mix', 'MergedCaloTruth'),
  superClusterThreshold = cms.double(4),
  simClusterTruthSrc = cms.InputTag('mix', 'MergedCaloTruth'),
  muonSrc = cms.InputTag('muons1stStep'),
  neutralHADThreshold = cms.double(0.25),
  gsfTrackSrc = cms.InputTag('electronGsfTracks'),
  trackTimeValueMap = cms.optional.InputTag,
  trackTimeErrorMap = cms.optional.InputTag,
  trackTimeQualityMap = cms.optional.InputTag,
  timingQualityThreshold = cms.optional.double,
  gsfTrackTimeValueMap = cms.optional.InputTag,
  gsfTrackTimeErrorMap = cms.optional.InputTag,
  gsfTrackTimeQualityMap = cms.optional.InputTag,
  mightGet = cms.optional.untracked.vstring
)
