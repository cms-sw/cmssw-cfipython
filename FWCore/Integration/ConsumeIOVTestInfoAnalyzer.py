import FWCore.ParameterSet.Config as cms

def ConsumeIOVTestInfoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ConsumeIOVTestInfoAnalyzer',
    esInputTag = cms.untracked.ESInputTag('', ''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
