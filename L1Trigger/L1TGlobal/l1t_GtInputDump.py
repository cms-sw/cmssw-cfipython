import FWCore.ParameterSet.Config as cms

def l1t_GtInputDump(*args, **kwargs):
  mod = cms.EDAnalyzer('l1t::GtInputDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
