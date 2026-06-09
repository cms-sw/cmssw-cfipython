import FWCore.ParameterSet.Config as cms

def TestGsfElectronConversionFinder(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGsfElectronConversionFinder',
    gsfElectrons = cms.InputTag('gedGsfElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
