import FWCore.ParameterSet.Config as cms

def SiStripPedestalsBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
