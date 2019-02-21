import FWCore.ParameterSet.Config as cms

candMergerCleanOthersByDR = cms.EDProducer('CandMergerCleanOthersByDR',
  coll1 = cms.InputTag('egammasForCoreTracking'),
  coll2 = cms.InputTag('jetsForCoreTracking'),
  maxDRToClean = cms.double(0.05)
)
