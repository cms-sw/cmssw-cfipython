import FWCore.ParameterSet.Config as cms

def MTDDigiContentDump(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDDigiContentDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
