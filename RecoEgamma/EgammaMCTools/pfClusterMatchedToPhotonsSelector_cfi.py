import FWCore.ParameterSet.Config as cms

pfClusterMatchedToPhotonsSelector = cms.EDProducer('PFClusterMatchedToPhotonsSelector',
  pfClustersTag = cms.InputTag('particleFlowClusterECAL'),
  trackingParticleTag = cms.InputTag('mix', 'MergedTrackTruth'),
  genParticleTag = cms.InputTag('genParticles'),
  maxDR2 = cms.double(0.010000000000000002),
  maxDEDR2 = cms.double(0.25),
  volumeZ_EB = cms.double(304.5),
  volumeRadius_EB = cms.double(123.8),
  volumeZ_EE = cms.double(317)
)
