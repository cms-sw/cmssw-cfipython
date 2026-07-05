import FWCore.ParameterSet.Config as cms

def TestBTLReadoutMap(*args, **kwargs):
  mod = cms.EDAnalyzer('TestBTLReadoutMap',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
