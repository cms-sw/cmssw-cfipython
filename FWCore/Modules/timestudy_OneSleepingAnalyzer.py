import FWCore.ParameterSet.Config as cms

def timestudy_OneSleepingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('timestudy::OneSleepingAnalyzer',
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
