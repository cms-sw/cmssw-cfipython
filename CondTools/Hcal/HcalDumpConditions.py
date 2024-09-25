import FWCore.ParameterSet.Config as cms

def HcalDumpConditions(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDumpConditions',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
