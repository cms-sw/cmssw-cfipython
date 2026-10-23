import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDepDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleDepDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
