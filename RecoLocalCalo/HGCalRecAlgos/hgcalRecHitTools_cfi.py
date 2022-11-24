import FWCore.ParameterSet.Config as cms

hgcalRecHitTools = cms.EDAnalyzer('HGCalTestRecHitTools',
  mightGet = cms.optional.untracked.vstring
)
