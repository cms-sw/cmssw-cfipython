import FWCore.ParameterSet.Config as cms

SiStripApprox2Clusters = cms.EDProducer('SiStripApprox2Clusters',
  inputApproxClusters = cms.InputTag('siStripClusters'),
  mightGet = cms.optional.untracked.vstring
)
