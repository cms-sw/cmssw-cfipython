import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDepDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleDepDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
