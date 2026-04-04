import FWCore.ParameterSet.Config as cms

def CSCDDUMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCDDUMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
