import FWCore.ParameterSet.Config as cms

SiStripApprox2ApproxClusters = cms.EDProducer('SiStripApprox2ApproxClusters',
  inputApproxClusters = cms.InputTag('siStripClusters'),
  approxVersion = cms.string('ORIGINAL'),
  mightGet = cms.optional.untracked.vstring
)
