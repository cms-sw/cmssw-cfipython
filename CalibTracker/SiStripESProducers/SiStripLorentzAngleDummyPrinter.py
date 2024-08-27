import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
