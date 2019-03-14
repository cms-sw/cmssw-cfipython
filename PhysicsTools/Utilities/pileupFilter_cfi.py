import FWCore.ParameterSet.Config as cms

pileupFilter = cms.EDFilter('PileUpFilter',
  pileupInfoSummaryInputTag = cms.InputTag('PileupSummaryInfo'),
  minPU = cms.double(0),
  maxPU = cms.double(80)
)
