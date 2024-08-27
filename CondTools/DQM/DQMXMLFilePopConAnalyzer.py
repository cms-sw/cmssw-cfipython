import FWCore.ParameterSet.Config as cms

def DQMXMLFilePopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DQMXMLFilePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
