import FWCore.ParameterSet.Config as cms

def DQMXMLFileEventSetupAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DQMXMLFileEventSetupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
