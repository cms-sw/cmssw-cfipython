import FWCore.ParameterSet.Config as cms

def SiStripFedCablingBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
