import FWCore.ParameterSet.Config as cms

def SimPFProducer(**kwargs):
  mod = cms.EDProducer('SimPFProducer',
    simClustersSrc = cms.InputTag('particleFlowClusterHGCalFromSimCl'),
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
    useTiming = cms.bool(False),
    useTimingQuality = cms.bool(False),
    trackTimeValueMap = cms.InputTag(''),
    trackTimeErrorMap = cms.InputTag(''),
    trackTimeQualityMap = cms.InputTag(''),
    timingQualityThreshold = cms.double(0),
    gsfTrackTimeValueMap = cms.InputTag(''),
    gsfTrackTimeErrorMap = cms.InputTag(''),
    gsfTrackTimeQualityMap = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
