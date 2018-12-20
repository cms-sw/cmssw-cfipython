import FWCore.ParameterSet.Config as cms

siStripBaselineComparator = cms.EDAnalyzer('SiStripBaselineComparator',
  srcClusters = cms.InputTag('siStripClusters'),
  srcClusters2 = cms.InputTag('moddedsiStripClusters')
)
