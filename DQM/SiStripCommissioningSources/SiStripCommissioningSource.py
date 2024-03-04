import FWCore.ParameterSet.Config as cms

def SiStripCommissioningSource(**kwargs):
  mod = cms.EDAnalyzer('SiStripCommissioningSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
