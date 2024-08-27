import FWCore.ParameterSet.Config as cms

def l1t_GtInputDump(**kwargs):
  mod = cms.EDAnalyzer('l1t::GtInputDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
