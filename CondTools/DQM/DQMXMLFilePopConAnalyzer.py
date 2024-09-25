import FWCore.ParameterSet.Config as cms

def DQMXMLFilePopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMXMLFilePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
