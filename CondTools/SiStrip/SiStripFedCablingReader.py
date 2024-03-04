import FWCore.ParameterSet.Config as cms

def SiStripFedCablingReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
