import FWCore.ParameterSet.Config as cms

def MaterialBudgetHcalAnalysis(**kwargs):
  mod = cms.EDAnalyzer('MaterialBudgetHcalAnalysis',
    nBinEta = cms.int32(260),
    nBinPhi = cms.int32(180),
    maxEta = cms.double(5.2),
    etaLow = cms.double(-5.2),
    etaHigh = cms.double(5.2),
    etaMinP = cms.double(5.2),
    etaMaxP = cms.double(0),
    etaLowMin = cms.double(0.783),
    etaLowMax = cms.double(0.87),
    etaMidMin = cms.double(2.65),
    etaMidMax = cms.double(2.868),
    etaHighMin = cms.double(2.868),
    etaHighMax = cms.double(3),
    labelMBCaloLabel = cms.InputTag('g4SimHits', 'HcalMatBCalo'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
