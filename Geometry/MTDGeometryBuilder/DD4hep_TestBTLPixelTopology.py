import FWCore.ParameterSet.Config as cms

def DD4hep_TestBTLPixelTopology(*args, **kwargs):
  mod = cms.EDAnalyzer('DD4hep_TestBTLPixelTopology',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
