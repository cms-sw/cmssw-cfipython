import FWCore.ParameterSet.Config as cms

def DQMXMLFileEventSetupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMXMLFileEventSetupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
