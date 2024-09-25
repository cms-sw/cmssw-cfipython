import FWCore.ParameterSet.Config as cms

def DTReadOutMappingPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTReadOutMappingPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
