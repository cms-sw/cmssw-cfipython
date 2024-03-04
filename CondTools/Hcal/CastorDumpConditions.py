import FWCore.ParameterSet.Config as cms

def CastorDumpConditions(**kwargs):
  mod = cms.EDAnalyzer('CastorDumpConditions',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
