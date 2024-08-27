import FWCore.ParameterSet.Config as cms

def SiStripBadChannelDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadChannelDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
