import FWCore.ParameterSet.Config as cms

def testEvtLoop(*args, **kwargs):
  mod = cms.EDAnalyzer('testEvtLoop',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
