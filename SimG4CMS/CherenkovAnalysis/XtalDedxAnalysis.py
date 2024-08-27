import FWCore.ParameterSet.Config as cms

def XtalDedxAnalysis(**kwargs):
  mod = cms.EDAnalyzer('XtalDedxAnalysis',
    caloHitSource = cms.InputTag('g4SimHits', 'EcalHitsEB'),
    moduleLabelTk = cms.string('g4SimHits'),
    energyMax = cms.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
