import FWCore.ParameterSet.Config as cms

def testEvtLoop(**kwargs):
  mod = cms.EDAnalyzer('testEvtLoop',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
