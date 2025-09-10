import FWCore.ParameterSet.Config as cms

def XtalDedxAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('XtalDedxAnalysis',
    caloHitSource = cms.InputTag('g4SimHits', 'EcalHitsEB'),
    moduleLabelTk = cms.string('g4SimHits'),
    energyMax = cms.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
