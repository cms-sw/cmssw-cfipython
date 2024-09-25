import FWCore.ParameterSet.Config as cms

def timestudy_OneSleepingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('timestudy::OneSleepingAnalyzer',
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
