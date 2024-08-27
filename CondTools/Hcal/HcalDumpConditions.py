import FWCore.ParameterSet.Config as cms

def HcalDumpConditions(**kwargs):
  mod = cms.EDAnalyzer('HcalDumpConditions',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
