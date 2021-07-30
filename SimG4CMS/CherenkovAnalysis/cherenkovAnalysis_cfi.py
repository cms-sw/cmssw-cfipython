import FWCore.ParameterSet.Config as cms

cherenkovAnalysis = cms.EDAnalyzer('CherenkovAnalysis',
  caloHitSource = cms.InputTag('g4SimHits', 'EcalHitsEB'),
  maxEnergy = cms.double(2),
  nBinsEnergy = cms.int32(50),
  mightGet = cms.optional.untracked.vstring
)
