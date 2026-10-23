import FWCore.ParameterSet.Config as cms

def l1t_GtRecordDump(*args, **kwargs):
  mod = cms.EDAnalyzer('l1t::GtRecordDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
