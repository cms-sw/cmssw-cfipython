import FWCore.ParameterSet.Config as cms

def RctDigiToRctText(*args, **kwargs):
  mod = cms.EDAnalyzer('RctDigiToRctText',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
