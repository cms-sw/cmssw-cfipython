import FWCore.ParameterSet.Config as cms

xtalDedxAnalysis = cms.EDAnalyzer('XtalDedxAnalysis',
  caloHitSource = cms.InputTag('g4SimHits', 'EcalHitsEB'),
  moduleLabelTk = cms.string('g4SimHits'),
  energyMax = cms.double(2),
  mightGet = cms.optional.untracked.vstring
)
