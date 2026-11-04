import FWCore.ParameterSet.Config as cms

mcZllMesonPhotonFilter = cms.EDFilter('MCZllMesonPhotonFilter',
  src = cms.InputTag('generator', 'unsmeared'),
  particleID = cms.int32(22),
  motherIDs = cms.vint32(
    111,
    221
  ),
  minPt = cms.double(5),
  clusterDeltaR = cms.double(0.1),
  minClusterPt = cms.double(10),
  minDileptonMass = cms.double(75),
  maxDileptonMass = cms.double(105),
  mightGet = cms.optional.untracked.vstring
)
