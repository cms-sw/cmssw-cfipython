import FWCore.ParameterSet.Config as cms

def MTDDigiDump(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
