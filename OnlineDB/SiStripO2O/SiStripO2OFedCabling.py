import FWCore.ParameterSet.Config as cms

def SiStripO2OFedCabling(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OFedCabling',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
