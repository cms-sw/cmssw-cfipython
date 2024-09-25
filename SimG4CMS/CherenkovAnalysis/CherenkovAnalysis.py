import FWCore.ParameterSet.Config as cms

def CherenkovAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('CherenkovAnalysis',
    caloHitSource = cms.InputTag('g4SimHits', 'EcalHitsEB'),
    maxEnergy = cms.double(2),
    nBinsEnergy = cms.int32(50),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
