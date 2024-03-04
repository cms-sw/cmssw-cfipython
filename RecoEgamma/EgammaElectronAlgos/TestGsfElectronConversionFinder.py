import FWCore.ParameterSet.Config as cms

def TestGsfElectronConversionFinder(**kwargs):
  mod = cms.EDAnalyzer('TestGsfElectronConversionFinder',
    gsfElectrons = cms.InputTag('gedGsfElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
