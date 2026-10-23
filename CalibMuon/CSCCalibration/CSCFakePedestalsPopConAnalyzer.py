import FWCore.ParameterSet.Config as cms

def CSCFakePedestalsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCFakePedestalsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
