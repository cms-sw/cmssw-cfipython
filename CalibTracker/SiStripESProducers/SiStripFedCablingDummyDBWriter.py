import FWCore.ParameterSet.Config as cms

def SiStripFedCablingDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
