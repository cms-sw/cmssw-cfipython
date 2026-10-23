import FWCore.ParameterSet.Config as cms

def SiStripO2OFedCabling(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripO2OFedCabling',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
